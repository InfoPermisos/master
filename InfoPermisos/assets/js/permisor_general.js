window.onscroll = function() {scrollFunction()};

/* Set the width of the sidebar to 250px (show it) */
function openNav() {
  document.getElementById("sidepanel").style.width = "250px";
}

/* Set the width of the sidebar to 0 (hide it) */
function closeNav() {
  document.getElementById("sidepanel").style.width = "0";
} 


function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("navBar").classList.add("scrolled")
  } else {
    document.getElementById("navBar").classList.remove("scrolled")
  }
} 