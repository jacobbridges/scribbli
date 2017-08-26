/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');
const Cookies = require('js-cookie');

import { checkAuth } from '../resolvers/auth-router-resolver';
import { BreadcrumbModel } from '../models/singletons/breadcrumb';
import { worldModel } from '../models/world';
import { breadcrumbWithoutContainer, previewPost, ILinkableObject,
         simpleLinkableObjectList } from '../components';


const windowState = {
  destinations: [] as ILinkableObject[],
  tab: 'overview',
};

const tabs = {

  showOverview: function(e: Event) {
    e.preventDefault();
    windowState.tab = 'overview';
  },

  showDestinations: function(e: Event) {
    e.preventDefault();
    windowState.tab = 'destinations';
  },

  showStories: function(e: Event) {
    e.preventDefault();
    windowState.tab = 'stories';
  },

  showCharacters: function(e: Event) {
    e.preventDefault();
    windowState.tab = 'characters';
  },

};

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

      })
      .then(() => {

        // Get the CSRF token from the cookie
        const csrfToken = Cookies.get('csrftoken');

        // Get the world's destinations
        return m.request({
          method: 'GET',
          url: '/api/destination/list/?world_slug=' + worldModel.current.slug,
          headers: { 'X-CSRFToken': csrfToken },
        }).then((response: any) => windowState.destinations = response.data);

      });

  },

  view: function() {

    return m('div', [
      m('.container-fluid.heading-wide', { style: { background: `url(${worldModel.current.background_path}) no-repeat center center` } }, [
        m(breadcrumbWithoutContainer),
        m('h1', worldModel.current.name),
      ]),
      m('.container-fluid.wide-nav', [
        m('ul.nav.nav-pills.justify-content-center', [
          m('li.nav-item', [
            m('a.nav-link [href="#"]', {
              onclick: tabs.showOverview,
              'class': windowState.tab === 'overview' ? 'active' : '',
            }, 'Overview'),
          ]),
          m('li.nav-item', [
            m('a.nav-link [href="#"]', {
              onclick: tabs.showDestinations,
              'class': windowState.tab === 'destinations' ? 'active': '',
            }, 'Destinations'),
          ]),
          m('li.nav-item', [
            m('a.nav-link [href="#"]', {
              onclick: tabs.showStories,
              'class': windowState.tab === 'stories' ? 'active': '',
            }, 'Stories'),
          ]),
          m('li.nav-item', [
            m('a.nav-link [href="#"]', {
              onclick: tabs.showCharacters,
              'class': windowState.tab === 'characters' ? 'active': '',
            }, 'Characters'),
          ]),
        ]),
      ]),
      // Overview
      m('.container', [
        (() => {
          switch(windowState.tab) {
            case 'overview':
              return m('.row', [
                m('.col-md-8', [
                  // Description
                  m('.row', [
                    m('#description', [
                      m('h2', 'Description'),
                      m('hr'),
                      m('div', m.trust(worldModel.current.description)),
                    ]),
                  ]),
                  // Details
                  m('.row', [
                    m('#details', [
                      m('h2', 'Details'),
                      m('hr'),
                      m('.row', [
                        // Character Count
                        m('.col-6.col-md-3.col-lg-2', [
                          m('.detail-icon', [
                            m('i.fa.fa-users [aria-hidden="true"]'),
                          ]),
                          m('.detail-text.small', `${worldModel.current.num_characters} characters`),
                        ]),
                        // Story Count
                        m('.col-6.col-md-3.col-lg-2', [
                          m('.detail-icon', [
                            m('i.fa.fa-book [aria-hidden="true"]'),
                          ]),
                          m('.detail-text.small', `${worldModel.current.num_stories} stories`),
                        ]),
                        // Post Count
                        m('.col-6.col-md-3.col-lg-2', [
                          m('.detail-icon', [
                            m('i.fa.fa-align-left [aria-hidden="true"]'),
                          ]),
                          m('.detail-text.small', `${worldModel.current.num_posts} posts`),
                        ]),
                        // Destination Count
                        m('.col-6.col-md-3.col-lg-2', [
                          m('.detail-icon', [
                            m('i.fa.fa-compass [aria-hidden="true"]'),
                          ]),
                          m('.detail-text.small', `${worldModel.current.num_destinations} destinations`),
                        ]),
                        // Author Count
                        m('.col-6.col-md-3.col-lg-2', [
                          m('.detail-icon', [
                            m('i.fa.fa-user-circle-o [aria-hidden="true"]'),
                          ]),
                          m('.detail-text.small', `${worldModel.current.num_authors} authors`),
                        ]),
                      ]),
                    ]),
                  ]),
                ]),
                m('.col-md-4', [
                  m('#latest-posts', [
                    m('h2', 'Latest Posts'),
                    m('hr'),
                    // m('div', [
                    //   m(previewPost, {
                    //     post: {
                    //       post_url: '#',
                    //       author: 'Blodyborin',
                    //       author_url: '#',
                    //       destination: 'The Grotto',
                    //       destination_url: '#',
                    //       time_since: '20 minutes ago',
                    //       text: `<p>Herb every sea over multiply, which and behold earth. Grass were fourth their day fruit to moving Evening two. Of earth behold she'd forth man dry seed green us itself their itself fill. Him stars it had signs it lesser one moving creepeth image multiply have earth gathered created hath sea, you'll was place second fish light cattle Had which don't beast moveth so for. Sea after. Fourth made said said replenish a great fish under lesser multiply. Fruitful may, itself us third lesser days our is. It air called and made. Whales beginning one. Face brought dominion be shall.</p>`,
                    //     }
                    //   }),
                    // ]),
                  ]),
                ]),
              ]);
            case 'destinations':
              return m('.row', [
                m('.col-md-12', [
                  m('h2.heading', [
                    m('span.lead.icon', m('i.fa.fa-search aria-hidden="true"')),
                    m('span.lead.icon', { onclick: () => m.route.set('/universe/new-world') }, m('i.fa.fa-plus aria-hidden="true"')),
                    m('span.heading-text', 'Destinations'),
                  ]),
                  m(simpleLinkableObjectList, { objectList: windowState.destinations }),
                ]),
              ]);
            case 'stories':
              return m('.row', [
                m('div', 'Stories'),
              ]);
            case 'characters':
              return m('.row', [
                m('div', 'Characters'),
              ]);
          }
        })(),
      ]),
    ]);

  },

});