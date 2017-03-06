/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');


export const hero = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    return m('.hero', vnode.attrs, [
      m('.container', vnode.children.length === 0
         ? m('h4', vnode.attrs['text'])
         : vnode.children,
      ),
    ]);

  }

};

export const darkHero = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    return m('.hero-dark', vnode.attrs, [
      m('.container', vnode.children.length === 0
         ? m('h4', vnode.attrs['text'])
         : vnode.children,
      ),
    ]);

  }

};