/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');

import * as Components from '../components';
import { BreadcrumbModel } from '../models/singletons/breadcrumb';
import { WriterModel as wm } from '../models/singletons/writer-data';
import { checkAuth } from '../resolvers/auth-router-resolver';


export const homeView = checkAuth({

  oninit: function() {

    BreadcrumbModel.Singleton.crumbs = [
      { name: m('i', { 'class': 'fa fa-home' }), path: '/home' },
    ];

  },

  view: function(vnode: Mithril.Vnode<any, any>) {

    const fabData: Components.IFAB = {
      buttons: [
        { name: 'Logout', icon: 'fa fa-sign-out', route: '' },
      ],
      mainIcon: 'fa fa-book',
    };

    const fullPageLayoutData: Components.IFullPageLayout = {
      breadcrumbs: m(Components.breadcrumb),
      pageHeading: 'Home Page',
      body: m('p', `Welcome home, ${wm.i.name}`),
      fab: m(Components.FAB, { fabData }),
    };

    return m(Components.FullPageLayout, { fullPageLayoutData });

    // return m('div', [
    //   m(Components.darkHero, [
    //     m('h4', `Welcome to Scribbli, ${wm.i.name}!`),
    //     m('nav.nav', [
    //       m('a.nav-link', { href: '/universe', oncreate: m.route.link }, 'Universe'),
    //       m('a.nav-link href=[/stories]', { oncreate: m.route.link }, 'Stories'),
    //       m('a.nav-link href=[/characters]', { oncreate: m.route.link }, 'Characters'),
    //       m('a.nav-link href=[/writers]', { oncreate: m.route.link }, 'Writers'),
    //       m(`a.nav-link href=[/writer/${wd.i().name}/worlds]`, { oncreate: m.route.link }, 'My Worlds'),
    //       m(`a.nav-link href=[/writer/${wd.i().name}]`, { oncreate: m.route.link }, 'My Profile'),
    //       m('a.nav-link.disabled href=[/activity]', { oncreate: m.route.link }, 'Site Activity'),
    //     ]),
    //   ]),
    //   // Universe
    // ]);

  }

});