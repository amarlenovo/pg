function getRandomColor(){
  var letters='0123456789ABCDEF';
  var color='#';
  for(var i=0;i<6;i++){
      var r1=Math.floor(Math.random()*16)
      color=color+letters[r1]
    }
    return color;
}


var b=document.querySelector('#but')
function changeColor(){
 b.style.background=getRandomColor()
 b.style.color='white'
}
setInterval(changeColor,200)
