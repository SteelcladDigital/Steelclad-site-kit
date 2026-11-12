(function(){
  // mobile menu
  var t=document.querySelector('.menu-toggle'),n=document.getElementById('nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});}

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

  // demo form (no GHL connection yet): never pretends to send
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var m=f.querySelector('.form-msg'); if(m){m.classList.add('show');}
    });
  });

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

  // preselect plan from ?plan= or #plan- hash
  var sel=document.getElementById('f-plan');
  if(sel){
    var h=(location.hash||'').replace('#plan-','');
    if(h){for(var i=0;i<sel.options.length;i++){if(sel.options[i].value===h){sel.selectedIndex=i}}}
  }
})();
