import { pseudonymRegexCheck, emailRegexCheck } from "../utils/validation";
const m = require('mithril');
const Cookies = require('js-cookie');

import { SiteApi } from '../siteapi';

// -------------------------------------------------------------------------------------------------
// Interfaces

export interface Writer {
  email: string;
  name: string;
  date_created: Date;
  unik?: string;
  password?: string;
}


// -------------------------------------------------------------------------------------------------
// Model

export const writerModel = {

  // Any error message regarding the writers
  error: '',

  // The current writer object
  current: {} as Writer,

  // Setters
  setName: (name: string) => writerModel.current.name = name,
  setEmail: (email: string) => writerModel.current.email = email,
  setDateCreated: (date_created: Date) => writerModel.current.date_created = date_created,
  setUnik: (unik: string) => writerModel.current.unik = unik,
  setPassword: (password: string) => writerModel.current.password = password,

  // Does the writer's name pass validation
  namePassValidation: () => {

    const name = writerModel.current.name;
    return (typeof name === 'string') && pseudonymRegexCheck(name) && name.length <= 100;

  },

  // Does the writer's email pass validation
  emailPassValidation: () => {

    const email = writerModel.current.email;
    return (typeof email === 'string') && emailRegexCheck(email) && email.length <= 200;

  },

  // Does the writer's password pass validation
  passwordPassValidation: () => {

    const password = writerModel.current.password;
    return (typeof password === 'string') && password.length >= 6 && password.length <= 50;

  },

  // Does the writer pass validation
  passValidation: () => {

    return writerModel.namePassValidation()
      && writerModel.emailPassValidation()
      && writerModel.passwordPassValidation();

  },

  // Create a new writer via the siteapi
  create: function (event: Event) {

    // Prevent the form from submitting
    event.preventDefault();

    // Get the data from the current writer
    const { email, name, password, unik } = writerModel.current;

    // Get the CSRF token from the cookie
    const csrfToken = Cookies.get('csrftoken');

    // Request the siteapi create a new writer with the current writer's information
    return m.request({
      method: 'POST',
      url: '/api/writer/',
      withCredentials: true,
      headers: { 'X-CSRFToken': csrfToken },
      data: { email, name, password, unik: (unik ? unik : null) },
    })
      .then(function(apiResponse: SiteApi.Response) {

        if (apiResponse.id === 'success') {

          // Assign the api response to type "successfully created writer"
          let successResponse = apiResponse as SiteApi.Responses.CreateWriter;

          // Create a reference to the created writer object in the response (for easy reference)
          const writerObj = successResponse.data[0].fields;

          // Parse the fields out into a Writer object
          writerModel.current = <Writer>{
            email: writerObj.email,
            name: writerObj.name,
            date_created: new Date(writerObj.date_created),
          };

          // TODO: NEED TO SET EMAIL TO STATE AND REDIRECT TO HOMEPAGE

        } else if (apiResponse.id === 'failure') {

          // Assign the api response to type "errored request"
          let failResponse = apiResponse as SiteApi.ErrorResponse;

          // Set the API error to the model's error
          writerModel.error = failResponse.data.message;

        } else {

          // If the code gets to here, the siteapi returned something unexpected
          writerModel.error = 'The siteapi returned an unexpected response!';

        }

      });

  },

};