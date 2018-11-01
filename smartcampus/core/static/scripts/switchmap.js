window.onload = function(){
    var btnGroup = document.getElementsByClassName("btn-group")[0];
    var myButton = btnGroup.getElementsByTagName("button");
    var myDiv = document.getElementsByClassName("map-canvas");

    for(var i = 0; i<myButton.length;i++){
        myButton[i].index = i;
        myButton[i].onclick = function(){
            for(var i = 0; i < myButton.length; i++){
                myButton[i].className="btn btn-default";
                myDiv[i].style.display="none";
            }
            this.className = "btn btn-danger";
            myDiv[this.index].style.display = "block";
        }
      }
}


