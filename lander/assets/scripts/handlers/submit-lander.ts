import { validateEmail } from '../utils/validation';
const TweenLite = require('../../vendor/TweenMax');
const Cookies = require('js-cookie');

interface WindowWithUserData extends Window {
  userData: any;
}

export const handleSubmitEmail = function(event: Event) {

  event.preventDefault();
  const requestInput = <HTMLInputElement>document.querySelector('.request-input');

  if (!validateEmail(requestInput.value, ['hemingway@gmail.com'])) {
    requestInput.style.color = '#f96377';
    requestInput.focus();
    requestInput.setSelectionRange(0, requestInput.value.length);
    return;
  }

  requestInput.style.color = 'white';
  document.getElementById('alpha-c').style.visibility = 'hidden';
  document.getElementById('once-upon-a-time').style.display = 'block';
  document.getElementById('lander').style.display = 'none';
  (<HTMLElement>document.querySelector('.attn')).style.display = 'none';
  (<HTMLElement>document.querySelector('.success-icon')).style.opacity = '1';
  TweenLite.to('body', 0, {backgroundColor:'white'});
  TweenLite.to('.title', 0, {color: '#2E3D48'});

  const req = new XMLHttpRequest();
  req.addEventListener('load', function() { console.log(this.responseText); });
  req.open('POST', '/api' + '/signup' + '/');
  const data = (<WindowWithUserData>window).userData;
  data['email'] = requestInput.value;
  req.setRequestHeader('Content-Type', 'application/json');
  const csrfToken = Cookies.get('csrftoken');
  req.setRequestHeader('X-CSRFToken', csrfToken);
  req.send(JSON.stringify(data));

};