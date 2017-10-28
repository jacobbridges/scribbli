/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');
const Cookies: Cookies.CookiesStatic = require('js-cookie');

import { isUndefined } from 'util';
import { SiteApi } from '../siteapi';
import { WriterModel as wm } from '../models/singletons/writer-data';


export const checkAuth = (view: Mithril.Component<any, any>) => ({

  onmatch: function() {

    // Get the JSON web token from the cookies
    const token = Cookies.get('a.t');

    // If the token could not be found, revert to the /login route
    if (!token) {

      console.log('No authentication token found, rerouting to /login!');
      m.route.set('/login');
      return;

    }

    console.log('Authentication token found!');
    // If the token was in the cookies, verify that the writer data exists
    if (isUndefined(wm.i.email) || isUndefined(wm.i.name || isUndefined(wm.i.scopes))) {

      console.log('User data not found in singleton, retrieving from siteapi...');

      // Get the CSRF token from the cookie
      const csrfToken = Cookies.get('csrftoken');

      // If the user's data could not be found, retrieve it from the API
      return m.request({
        method: 'POST',
        url: '/api/login/',
        headers: { 'X-CSRFToken': csrfToken },
        withCredentials: true,
      }).then((apiResponse: SiteApi.Response<any>) => {

        if (apiResponse.success === true) {

          console.log('Got data!', apiResponse.data);
          let successResponse = apiResponse as SiteApi.Response<SiteApi.Elements.WriterData>;
          wm.i.email = successResponse.data.email;
          wm.i.name = successResponse.data.name;
          wm.i.scopes = successResponse.data.scopes;

          document.querySelector('body').className = 'app';
          return view;

        } else if (apiResponse.success === false) {

          console.log('There was an error retrieving the writers data!', apiResponse);
          m.route.set('/login');

        } else {

          console.log('Siteapi did not response as expected..');
          m.route.set('/login');

        }

      });

    }

    document.querySelector('body').className = 'app';
    return view;

  }

});