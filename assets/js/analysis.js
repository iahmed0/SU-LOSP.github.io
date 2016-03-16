(function() {
  // Dynamically generate the submenu
  var nav = document.getElementById('play-sections');
  var titles = document.querySelectorAll('article .content h1');
  Array.forEach(titles, function(title) {
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.setAttribute('href', '#' + title.getAttribute('id'));
    a.innerHTML = title.innerHTML;
    li.appendChild(a);
    nav.appendChild(li);
  });
})();
