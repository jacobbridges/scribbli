const m = require('mithril');

import { SiteApi } from '../siteapi';

export const invitationModel = {

  // The current invitation object
  current: <SiteApi.Elements.Invitation>null,

  // Retrieve an invitation from the siteapi
  load: function(unik: string) {

    return m.request({
      method: 'GET',
      url: '/api/invitation/' + encodeURIComponent(unik),
      withCredentials: true,
    })
      // .then(function(apiResponse: any) { apiResponse.data = JSON.parse(apiResponse.data); return apiResponse; })
      .then(function(apiResponse: SiteApi.Responses.Invitation) {

        if (apiResponse.id === 'success')
          invitationModel.current = apiResponse.data[0].fields;
        else
          invitationModel.current = null;

      });

  },

};