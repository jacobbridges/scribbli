/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');
const Cookies = require('js-cookie');

import { pseudonymRegexCheck, emailRegexCheck } from '../utils/validation';
import { WriterModel as wm } from './singletons/writer-data';
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
    return (typeof name === 'string') && pseudonymRegexCheck(name) && name.length <= 40;

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

    return writerModel.namePassValidation() &&
      writerModel.emailPassValidation() &&
      writerModel.passwordPassValidation();

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
      .then(function(apiResponse: SiteApi.Response<any>) {

        if (apiResponse.success === true) {

          // Assign the api response to type "successfully created writer"
          let successResponse = apiResponse as SiteApi.Response<SiteApi.Model<SiteApi.Elements.Writer>[]>;

          // Create a reference to the created writer object in the response (for easy reference)
          const writerObj = successResponse.data[0].fields;

          // Parse the fields out into a Writer object
          writerModel.current = <Writer>{
            email: writerObj.email,
            name: writerObj.name,
            date_created: new Date(writerObj.date_created),
          };

          // Set the writer's email to local storage then redirect to login page
          wm.i.email = writerObj.email;
          m.route.set('/login');
          return; // Return to ensure no more code is ran in this function

        } else if (apiResponse.success === false) {

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

  // Authenticate against the site api
  login: (event: Event) => {

    // Prevent the form from submitting
    event.preventDefault();

    // Get the data from the current writer
    const { email, password } = writerModel.current;

    // Get the CSRF token from the cookie
    const csrfToken = Cookies.get('csrftoken');

    // Attempt to authenticate against the siteapi
    return m.request({
      method: 'POST',
      url: '/api/login/',
      headers: { 'X-CSRFToken': csrfToken },
      data: { email, password },
    }).then((apiResponse: SiteApi.Response<any>) => {

      if (apiResponse.success === true) {

        // 1. Store select information from the web token in local storage
        let successReponse = apiResponse as SiteApi.Response<SiteApi.Elements.WriterData>;
        wm.i.name = successReponse.data.name;
        wm.i.email = successReponse.data.email;
        wm.i.scopes = successReponse.data.scopes;

        // 2. Route to the homepage
        m.route.set('/home');
        return;

      } else if (apiResponse.success === false) {

        let failedResponse = apiResponse as SiteApi.ErrorResponse;
        writerModel.error = failedResponse.data.message;

      } else {

        writerModel.error = 'The server had a hiccup. Try again later.';

      }

    }).catch((err: any) => {

      writerModel.error = 'The server had a hiccup. Try again later.';
      console.error('Server had an error!', err);

    });

  },

};