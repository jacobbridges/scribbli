import { isUndefined } from "util";
const m = require('mithril');
const Cookies: Cookies.CookiesStatic = require('js-cookie');

import { SiteApi } from '../siteapi';
import { writerDataSingleton as wd } from '../models/singletons/writer-data';

interface MithrilView {
  view(...args: any[]): Mithril.VirtualElement;
}

export const checkAuth = (view: MithrilView) => ({

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
    if (isUndefined(wd.i().email) || isUndefined(wd.i().name || isUndefined(wd.i().scopes))) {

      console.log('User data not found in singleton, retrieving from siteapi...');

      // Get the CSRF token from the cookie
      const csrfToken = Cookies.get('csrftoken');

      // If the user's data could not be found, retrieve it from the API
      return m.request({
        method: 'POST',
        url: '/api/login/',
        headers: { 'X-CSRFToken': csrfToken },
        withCredentials: true,
      }).then((apiResponse: SiteApi.Response) => {

        if (apiResponse.id === 'success') {

          console.log('Got data!', apiResponse.data);
          let successResponse = apiResponse as SiteApi.Responses.GetWriterData;
          wd.i().email = successResponse.data.email;
          wd.i().name = successResponse.data.name;
          wd.i().scopes = successResponse.data.scopes;

          return view;

        } else if (apiResponse.id === 'failure') {

          console.log('There was an error retrieving the writers data!', apiResponse);
          m.route.set('/login');

        } else {

          console.log('Siteapi did not response as expected..');
          m.route.set('/login');

        }

      });

    }

    return view;

  }

});