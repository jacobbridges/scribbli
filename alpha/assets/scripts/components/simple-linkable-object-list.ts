/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');
import { truncate } from 'lodash';


// -------------------------------------------------------------------------------------------------
// Interfaces

export interface ILinkableObject {
  name: string;
  url: string;
  description: string;
  time_since: string;
  author: string;
}


export const simpleLinkableObjectList = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    const objectList = vnode.attrs.objectList as ILinkableObject[];

    return m('.row', [
      m('.list-group', objectList.map((object: ILinkableObject) => {
        return m('a.list-group-item.list-group-item-action.flex-column.align-items-start', { href: object.url, oncreate: m.route.link }, [
          m('.d-flex.w-100.justify-content-between', [
            m('h5.mb-1', object.name),
            m('small', object.time_since),
          ]),
          m('p.mb-1', truncate(m.trust(object.description))),
          m('small', `Created by ${object.author}`),
        ]);
      })),
    ]);

  }

  /*

  <div class="list-group">
  <a href="#" class="list-group-item list-group-item-action flex-column align-items-start active">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small>3 days ago</small>
    </div>
    <p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
    <small>Donec id elit non mi porta.</small>
  </a>
  <a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-muted">3 days ago</small>
    </div>
    <p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
    <small class="text-muted">Donec id elit non mi porta.</small>
  </a>
  <a href="#" class="list-group-item list-group-item-action flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-muted">3 days ago</small>
    </div>
    <p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
    <small class="text-muted">Donec id elit non mi porta.</small>
  </a>
</div>

   */

};