(function() {
  // Dynamically generate the submenu
  var nav = document.getElementById('play-sections');
  var titles = document.querySelectorAll('article .content h1');
  for (var i = 0; i < titles.length; i++) {
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.setAttribute('href', '#' + titles[i].getAttribute('id'));
    a.innerHTML = titles[i].innerHTML;
    li.appendChild(a);
    nav.appendChild(li);
  }

  window.onscroll = function(e) {
    var top = window.scrollY;
    var navLis = nav.querySelectorAll('li');
    for (var i = 0; i < titles.length; i++) {
      console.log(top, titles[i], titles[i].offsetTop);
      if (titles[i].offsetTop < top) {
        for (var j = 0; j < navLis.length; j++) {
          if (i == j) {
            navLis[j].classList.add('active');
          } else {
            navLis[j].classList.remove('active');
          }
        }
      }
    }
  };
})();
