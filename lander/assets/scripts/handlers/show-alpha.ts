const TweenLite = require('../../vendor/TweenMax');

export const handleShowAlpha = function(event: Event) {

  document.getElementById('alpha-c').style.visibility = 'visible';
  document.getElementById('once-upon-a-time').style.display = 'none';
  document.getElementById('lander').style.display = 'block';
  TweenLite.to("body", 0, {backgroundColor:"#2E3D48"});
  TweenLite.to(".title", 0, {color: "white"});
  const alphaInput = <HTMLInputElement>document.querySelector('.request-input');
  alphaInput.focus();
  alphaInput.setSelectionRange(0, alphaInput.value.length);
  this.onclick = null;

};