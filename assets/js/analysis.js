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
})();
