/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');

import { checkAuth } from '../resolvers/auth-router-resolver';
import { BreadcrumbModel } from '../models/singletons/breadcrumb';
import { worldModel } from '../models/world';
import { breadcrumbWithoutContainer, previewPost } from '../components';


const tabs = {

  overview: true,
  destinations: false,
  stories: false,
  characters: false,

  showOverview: function(e: Event) {
    e.preventDefault();
    tabs.overview = true;
    tabs.destinations = tabs.stories = tabs.characters = false;
  },

  showDestinations: function(e: Event) {
    e.preventDefault();
    tabs.destinations = true;
    tabs.overview = tabs.stories = tabs.characters = false;
  },

  showStories: function(e: Event) {
    e.preventDefault();
    tabs.stories = true;
    tabs.overview = tabs.destinations = tabs.characters = false;
  },

  showCharacters: function(e: Event) {
    e.preventDefault();
    tabs.characters = true;
    tabs.overview = tabs.destinations = tabs.stories = false;
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
              'class': tabs.overview ? 'active' : '',
            }, 'Overview'),
          ]),
          m('li.nav-item', [
            m('a.nav-link [href="#"]', {
              onclick: tabs.showDestinations,
              'class': tabs.destinations ? 'active': '',
            }, 'Destinations'),
          ]),
          m('li.nav-item', [
            m('a.nav-link [href="#"]', {
              onclick: tabs.showStories,
              'class': tabs.stories ? 'active': '',
            }, 'Stories'),
          ]),
          m('li.nav-item', [
            m('a.nav-link [href="#"]', {
              onclick: tabs.showCharacters,
              'class': tabs.characters ? 'active': '',
            }, 'Characters'),
          ]),
        ]),
      ]),
      // Overview
      m('.container', { style: { display: tabs.overview ? 'block' : 'none' } }, [
        m('.row', [
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
        ]),
      ]),
      // Destinations
      m('.container', { style: { display: tabs.destinations ? 'block' : 'none' } }, [
        m('.row', [
          m('div', 'Destinations'),
        ]),
      ]),
      // Stories
      m('.container', { style: { display: tabs.stories ? 'block' : 'none' } }, [
        m('.row', [
          m('div', 'Stories'),
        ]),
      ]),
      // Characters
      m('.container', { style: { display: tabs.characters ? 'block' : 'none' } }, [
        m('.row', [
          m('div', 'Characters'),
        ]),
      ]),
    ]);

  },

});