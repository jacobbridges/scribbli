/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');


// -------------------------------------------------------------------------------------------------
// Interfaces

export interface WorldTileData {
  name: string;
  slug: string;
  is_public: boolean;
  thumbnail: string;
  character_count: number;
  story_count: number;
  last_active: string;
}


export const worldTile = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    const world = vnode.attrs.world as WorldTileData;

    return m('.world.col-sm-3', {
      style: {
        background: `url(${world.thumbnail}) no-repeat center center`,
        backgroundSize: 'cover',
      },
      onclick: () => m.route.set(`/world/${world.slug}`),
      ...vnode.attrs }, [
      m('h4', world.name),
      m('i.fa', {
        className: world.is_public
          ? 'fa-unlock-alt privacy-public'
          : 'fa-lock privacy-mine',
        'aria-hidden': true,
      }),
      m('.info', [
        m('span.number-characters', [
          m('i.fa.fa-user', { 'aria-hidden': true }),
          world.character_count.toString(),
        ]),
        m('span.number-stories', [
          m('i.fa.fa-book', { 'aria-hidden': true }),
          world.story_count.toString(),
        ]),
        m('span.last-activity', [
          m('i.fa.fa-clock-o', { 'aria-hidden': true }),
          world.last_active,
        ]),
      ]),
    ]);

  }

};