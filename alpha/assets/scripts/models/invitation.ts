/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');

import { SiteApi } from '../siteapi';

export const invitationModel = {

  // Has the invitation been loaded yet?
  isLoaded: false,

  // Any error regarding the invitations
  error: <string>null,

  // The current invitation object
  current: <SiteApi.Elements.Invitation>null,

  // Retrieve an invitation from the siteapi
  load: function(unik: string) {

    return m.request({
      method: 'GET',
      url: '/api/invitation/' + encodeURIComponent(unik),
      withCredentials: true,
    })
      .then(function(apiResponse: SiteApi.Response<SiteApi.Model<SiteApi.Elements.Invitation>[]>) {

        if (apiResponse.success === true)
          invitationModel.current = apiResponse.data[0].fields;
        else
          invitationModel.current = null;

        invitationModel.isLoaded = true;

      }).catch(() => {

        invitationModel.error = 'Invitation does not exist!';
        invitationModel.current = null;
        invitationModel.isLoaded = true;

      });

  },

};