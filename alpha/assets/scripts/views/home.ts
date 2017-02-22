const m = require('mithril');

import * as Components from '../components';
import { writerDataSingleton as wd } from '../models/singletons/writer-data';
import { checkAuth } from '../resolvers/auth-router-resolver';


export const homeView = checkAuth({

  view: function(vnode: Mithril.VirtualElement) {

    return m('div', [
      m(Components.darkHero, [
        m('h4', `Welcome to Scribbli, ${wd.i().name}!`),
        m('nav.nav', [
          // m('a.nav-link href=[/universe]', { oncreate: m.route.link }, 'Universe'),
          // m('a.nav-link href=[/stories]', { oncreate: m.route.link }, 'Stories'),
          // m('a.nav-link href=[/characters]', { oncreate: m.route.link }, 'Characters'),
          // m('a.nav-link href=[/writers]', { oncreate: m.route.link }, 'Writers'),
          // m(`a.nav-link href=[/writer/${wd.i().name}/worlds]`, { oncreate: m.route.link }, 'My Worlds'),
          // m(`a.nav-link href=[/writer/${wd.i().name}]`, { oncreate: m.route.link }, 'My Profile'),
          // m('a.nav-link.disabled href=[/activity]', { oncreate: m.route.link }, 'Site Activity'),
        ]),
      ]),
      // Universe
    ]);

  }

});