// Create a "close" button and append it to each list item
var myNodelist = index.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = index.createElement("SPAN");
  var txt = index.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);
