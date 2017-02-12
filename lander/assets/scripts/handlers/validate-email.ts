import { validateEmail } from "../utils/validation";

export const handleEmailValidation = function(event: Event) {

  // If email is invalid, change the text color to red
  if (!validateEmail(this.value)) {
    this.style.color = '#f96377';
    return;
  }

  // If the email is valid, make it white
  this.style.color = 'white';

};