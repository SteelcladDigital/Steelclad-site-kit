(function(){
  // mobile menu
  var t=document.querySelector('.menu-toggle'),n=document.getElementById('nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o);
    if(o){n.style.setProperty('--navtop',Math.max(0,n.getBoundingClientRect().top)+'px')}});}
  // mobile: Services / Service Area open as accordions (tap to expand) instead of navigating, so every menu item stays reachable
  var mq=window.matchMedia('(max-width:1020px)');
  document.querySelectorAll('.nav .nl').forEach(function(a){
    var dd=a.nextElementSibling; if(!dd||!dd.classList.contains('dropdown'))return;
    a.addEventListener('click',function(e){if(!mq.matches)return;e.preventDefault();var o=a.parentNode.classList.toggle('dd-open');a.setAttribute('aria-expanded',o)});
  });

  // tier finder (config-driven: each radio has data-tier; tiers JSON in data-tiers)
  var q=document.getElementById('plan-finder');
  if(q){
    var tiers=JSON.parse(q.getAttribute('data-tiers')||'[]'),order=tiers.map(function(t){return t.slug});
    q.addEventListener('change',function(){
      var sets=q.querySelectorAll('fieldset'),votes={},answered=0;
      sets.forEach(function(fs){var c=fs.querySelector('input:checked');if(c){answered++;votes[c.dataset.tier]=(votes[c.dataset.tier]||0)+1}});
      if(answered<sets.length)return;
      var pick=null;order.forEach(function(sl){if(votes[sl]&&(!pick||votes[sl]>=votes[pick]))pick=sl});
      var t=tiers.filter(function(x){return x.slug===pick})[0];if(!t)return;
      var r=document.getElementById('quiz-result');
      r.querySelector('h3').textContent=(q.getAttribute('data-prefix')||'We\u2019d recommend: ')+t.name;
      r.querySelector('p').textContent=t.why;
      r.classList.add('show');
    });
  }

  //@@GHL-LINE demo form (no GHL connection yet): never pretends to send
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var m=f.querySelector('.form-msg'); if(m){m.classList.add('show');}
    });
  });

  //@@GHL-START
  // native form captured by the GoHighLevel External Tracking script.
  // The tracking script listens for the submit event; we wait a moment so it can send, then confirm.
  // Spam bots that fill the hidden "website" field are dropped. If the tracking script never loaded
  // (ad blocker, outage) the visitor is told to call/text instead of seeing a false "sent".
  document.querySelectorAll('form[data-native-ghl]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var hp=f.querySelector('[name=website]');
      if(hp&&hp.value){return;}
      var btn=f.querySelector('button[type=submit]'); if(btn){btn.disabled=true;}
      var loaded=(performance.getEntriesByType('resource')||[]).some(function(r){
        return /external-tracking|leadconnector|msgsndr|link\./i.test(r.name)&&r.responseEnd>0&&(r.transferSize>0||r.decodedBodySize>0||r.duration>0);
      });
      setTimeout(function(){
        var ok=f.querySelector('.form-msg'),err=f.querySelector('.form-err');
        if(loaded){ if(ok)ok.classList.add('show'); f.reset(); }
        else { if(err)err.classList.add('show'); if(btn)btn.disabled=false; }
      },1200);
    });
  });

  //@@GHL-END
  // first-touch attribution: remember how the visitor first arrived (UTMs, click IDs, referrer, landing page)
  // so a lead that converts three pages later still carries its source. Storage can be blocked: never fatal.
  var KEY='sk_attr',attr={};
  try{attr=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
  try{
    var qs=new URLSearchParams(location.search),seen=false;
    ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','fbclid'].forEach(function(k){if(qs.get(k)){seen=true}});
    if(seen||!attr.landing_page){
      attr={landing_page:location.href,referrer:document.referrer||'(direct)'};
      ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','fbclid'].forEach(function(k){if(qs.get(k))attr[k]=qs.get(k)});
      try{localStorage.setItem(KEY,JSON.stringify(attr))}catch(e){}
    }
  }catch(e){}
  document.querySelectorAll('[data-track]').forEach(function(i){
    var k=i.getAttribute('data-track');i.value=k==='page'?location.href:(attr[k]||'');
  });

  // Web3Forms: post with fetch, show a real success or error message (never a false "sent"),
  // fire a GA4/GTM 'generate_lead' event, then go to the thank-you page if one is set.
  // Without JavaScript the form still posts to Web3Forms and its redirect field takes over.
  document.querySelectorAll('form[data-web3forms]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var bc=f.querySelector('[name=botcheck]'); if(bc&&bc.checked){return;}
      var btn=f.querySelector('button[type=submit]'),ok=f.querySelector('.form-msg'),err=f.querySelector('.form-err');
      if(btn){btn.disabled=true;btn.dataset.label=btn.textContent;btn.textContent='Sending…';}
      if(err)err.classList.remove('show');
      var data={};new FormData(f).forEach(function(v,k){if(k!=='redirect')data[k]=v});
      fetch(f.action,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(data)})
        .then(function(r){return r.json().catch(function(){return {}}).then(function(j){return r.ok&&j.success!==false})})
        .then(function(sent){
          if(!sent)throw new Error('not sent');
          window.dataLayer=window.dataLayer||[];
          window.dataLayer.push({event:'generate_lead',form_name:data.form||'',lead_source:data.utm_source||data.referrer||''});
          var to=f.getAttribute('data-thanks');
          if(to){setTimeout(function(){location.href=to},400);return;}
          if(ok)ok.classList.add('show'); f.reset();
          if(btn){btn.textContent=btn.dataset.label;}
        })
        .catch(function(){
          if(err)err.classList.add('show');
          if(btn){btn.disabled=false;btn.textContent=btn.dataset.label;}
        });
    });
  });

  // reviews carousel: rotate one card at a time, loop, pause on hover/focus/touch, honour reduced motion
  document.querySelectorAll('.review-carousel').forEach(function(rc){
    var tr=rc.querySelector('.rc-track'), cards=tr.children, dots=rc.querySelector('.rc-dots'), i=0, timer=null, paused=false;
    var iv=parseInt(rc.dataset.interval,10)||6000, reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
    function perView(){return Math.max(1,Math.round(tr.clientWidth/(cards[0].getBoundingClientRect().width||1)));}
    function maxI(){return Math.max(0,cards.length-perView());}
    function go(n){i=n>maxI()?0:(n<0?maxI():n);tr.scrollTo({left:cards[i].offsetLeft-cards[0].offsetLeft,behavior:reduce?'auto':'smooth'});mark();}
    function build(){dots.innerHTML='';for(var k=0;k<=maxI();k++){var b=document.createElement('button');b.type='button';b.tabIndex=-1;(function(k){b.onclick=function(){go(k);restart();};})(k);dots.appendChild(b);}mark();}
    function mark(){[].forEach.call(dots.children,function(b,k){b.setAttribute('aria-current',k===i?'true':'false');});}
    function restart(){clearInterval(timer);if(!reduce&&!paused)timer=setInterval(function(){go(i+1);},iv);}
    rc.querySelector('.rc-prev').onclick=function(){go(i-1);restart();};
    rc.querySelector('.rc-next').onclick=function(){go(i+1);restart();};
    tr.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){e.preventDefault();go(i+1);restart();}if(e.key==='ArrowLeft'){e.preventDefault();go(i-1);restart();}});
    var st;tr.addEventListener('scroll',function(){clearTimeout(st);st=setTimeout(function(){var x=tr.scrollLeft,b=0,d=1e9;for(var k=0;k<cards.length;k++){var dd=Math.abs(cards[k].offsetLeft-cards[0].offsetLeft-x);if(dd<d){d=dd;b=k;}}i=Math.min(b,maxI());mark();},120);});
    ['mouseenter','focusin','touchstart'].forEach(function(ev){rc.addEventListener(ev,function(){paused=true;clearInterval(timer);},{passive:true});});
    ['mouseleave','focusout'].forEach(function(ev){rc.addEventListener(ev,function(){paused=false;restart();});});
    window.addEventListener('resize',function(){build();});
    build();restart();
  });

  // preselect plan from #plan-<slug> (links from plan cards)
  var h=(location.hash||'').replace('#plan-','');
  if(h){document.querySelectorAll('select[name=plan]').forEach(function(sel){
    for(var i=0;i<sel.options.length;i++){if(sel.options[i].value===h){sel.selectedIndex=i}}
  });}
})();
