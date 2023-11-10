var canvas = document.getElementById('myCanvas');
var context = canvas.getContext('2d');

context.strokeStyle = '#FF0000';    //  Color
context.beginPath('');  //  Start a new path 
context.moveTo(100,100);
context.lineTo(200,300);
context.strokeStyle();  //  Draw a red line

context.fillStyle = "#0000FF"
context.beginPath();
context.rect(100,150,300,200);
context.fill(); //  Fill the rectangle with a blue color