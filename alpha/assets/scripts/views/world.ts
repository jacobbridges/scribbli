/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');

import { checkAuth } from '../resolvers/auth-router-resolver';
import { BreadcrumbModel } from '../models/singletons/breadcrumb';
import { worldModel } from '../models/world';
import { breadcrumbWithoutContainer } from '../components';


export const worldView = checkAuth({

  oninit: function(vnode: Mithril.Vnode<any, any>) {

    // Get the current world slug
    const worldSlug = vnode.attrs.slug;

    // Check if the world model has data.
    // If the world model has data, this would mean that the user was redirected from some place
    // which had the world data and decided to forward it along to save the SPA another XHR request.
    if (worldModel.current.slug) {

      // Verify that the slug in the world model matches the slug of the current url
      if (worldModel.current.slug === worldSlug) {

        // Make breadcrumbs and return
        BreadcrumbModel.Singleton.crumbs = [
          { name: 'Home', path: '/home' },
          { name: 'Universe', path: '/universe' },
          { name: worldModel.current.name, path: `/world/${worldModel.current.slug}` },
        ];

        return;

      }

    }

    // In all other cases the current world must be retrieved from the siteapi
    return worldModel.get({ slug: worldSlug })
      .then(() => {

        // Make breadcrumbs
        BreadcrumbModel.Singleton.crumbs = [
          { name: 'Home', path: '/home' },
          { name: 'Universe', path: '/universe' },
          { name: worldModel.current.name, path: `/world/${worldModel.current.slug}` },
        ];

      });

  },

  view: function() {

    return m('div', [
      m('.container-fluid.heading-wide', {
        style: { background: `url(${worldModel.current.background_path}) no-repeat center center` }
      }, [
        m(breadcrumbWithoutContainer),
        m('h1', worldModel.current.name),
      ]),
    ]);

  },

});