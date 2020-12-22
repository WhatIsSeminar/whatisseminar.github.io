if (screen.width <= 699) {
  var x;
  x = document.getElementsByClassName("navbar-brand");
  x[0].innerHTML = "w?S";
  x = document.getElementsByClassName("col-md-2");
  var i;
  for (i = 0; i < x.length; i++) {
    x[i].style="text-align:left;";
  }
  x = document.getElementsByClassName("display-3");
  x[0].className="";
}
