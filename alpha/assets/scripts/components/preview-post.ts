/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');


// -------------------------------------------------------------------------------------------------
// Interfaces

export interface PreviewPostData {
  post_url: string;
  author: string;
  author_url: string;
  destination: string;
  destination_url: string;
  time_since: string;
  text: string;
}


export const previewPost = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    const post = vnode.attrs.post as PreviewPostData;

    return m('.preview-post', [
      m('div', [
        m('span.character', [
          m('a', { href: post.author_url, oncreate: m.route.link }, post.author),
          m.trust(' in '),
        ]),
        m('span.place', [
          m('a', { href: post.destination_url, oncreate: m.route.link }, post.destination),
          m.trust(', '),
        ]),
        m('span.when', post.time_since),
      ]),
      m.trust(post.text),
      m('a.see-post', { href: post.post_url, oncreate: m.route.link }, [
        'See full post',
        m('i.fa.fa-long-arrow-right [aria-hidden="true"]'),
      ]),
    ]);

  }

};