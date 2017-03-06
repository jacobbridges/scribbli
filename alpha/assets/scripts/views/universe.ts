/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');

import { checkAuth } from '../resolvers/auth-router-resolver';
import { BreadcrumbModel } from '../models/singletons/breadcrumb';
import { breadcrumb } from '../components';


export const universeView = checkAuth({

  oninit: function() {

    BreadcrumbModel.Singleton.crumbs = [
      { name: 'Home', path: '/home' },
      { name: 'Universe', path: '/universe' },
    ];

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
    ]);

  },

});