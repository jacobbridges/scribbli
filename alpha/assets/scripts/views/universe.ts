/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');
const Cookies = require('js-cookie');

import { checkAuth } from '../resolvers/auth-router-resolver';
import { BreadcrumbModel } from '../models/singletons/breadcrumb';
import { breadcrumb, worldTile, IWorldTileData } from '../components';


const windowState = {
  worlds: [] as IWorldTileData[],
};

export const universeView = checkAuth({

  oninit: function() {

    BreadcrumbModel.Singleton.crumbs = [
      { name: 'Home', path: '/home' },
      { name: 'Universe', path: '/universe' },
    ];

    // Get the CSRF token from the cookie
    const csrfToken = Cookies.get('csrftoken');

    // Create the siteapi request
    return m.request({
      method: 'GET',
      url: '/api/universe/',
      headers: { 'X-CSRFToken': csrfToken },
    }).then((response: any) => windowState.worlds = response.data);

  },

  view: function() {

    return m('div', [
      m(breadcrumb),
      m('.container', [
        m('.heading', [
          m('h1', [
            m('span.lead.icon', m('i.fa.fa-search aria-hidden="true"')),
            m('span.lead.icon', { onclick: () => m.route.set('/universe/new-world') }, m('i.fa.fa-plus aria-hidden="true"')),
            m('span.heading-text', 'Universe'),
            m('input.search-input', { type: 'text' }),
          ]),
        ]),
      ]),
      // Worlds
      m('.container', [
        m('.row', windowState.worlds.map((world: IWorldTileData) => m(worldTile, { world }))),
      ]),
    ]);

  },

});