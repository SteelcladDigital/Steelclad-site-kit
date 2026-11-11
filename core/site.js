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

  // demo form (only when no GHL form is configured)
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var m=f.querySelector('.form-msg'); if(m){m.classList.add('show');}
    });
  });

  // preselect plan from ?plan= or #plan- hash
  var sel=document.getElementById('f-plan');
  if(sel){
    var h=(location.hash||'').replace('#plan-','');
    if(h){for(var i=0;i<sel.options.length;i++){if(sel.options[i].value===h){sel.selectedIndex=i}}}
  }
})();
