import { handleShowAlpha, handleSubmitEmail, handleEmailValidation } from "./handlers";
import { typeWriter } from "./modules/typewriter";

/**
 * When the DOM loads, add all event listeners.
 */
document.addEventListener('DOMContentLoaded', function(event) {

  // Start typewriter animation after a second delay
  setTimeout(() => typeWriter(document.getElementById('typed'), 'Once upon a time'), 1000);

  // Event listener for showing alpha request form
  document.getElementById("show-alpha-form").addEventListener('click', handleShowAlpha);
  // Event listener for validating email address
  document.getElementById('email').addEventListener('keyup', handleEmailValidation);
  // Event listener for submitting email address
  document.getElementById("request-submit").addEventListener('click', handleSubmitEmail);

});