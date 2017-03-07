/// <reference path="../interfaces/mithril.d.ts" />
import { BreadcrumbModel } from '../models/singletons/breadcrumb';


const m = require('mithril');


export const breadcrumb = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    return m('.navbar', vnode.attrs, [
      m('.container', [
        m('ol.breadcrumb', BreadcrumbModel.Singleton.crumbs.map((breadcrumb, index) => {

          if (index === BreadcrumbModel.Singleton.crumbs.length - 1)
            return  m('li.breadcrumb-item.active', breadcrumb.name);
          return m('li.breadcrumb-item', [
            m('a', { href: breadcrumb.path, oncreate: m.route.link }, breadcrumb.name),
          ]);

        })),
      ]),
    ]);

  }

};

export const breadcrumbWithoutContainer = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    return m('.navbar', vnode.attrs, [
      m('ol.breadcrumb', BreadcrumbModel.Singleton.crumbs.map((breadcrumb, index) => {

        if (index === BreadcrumbModel.Singleton.crumbs.length - 1)
          return  m('li.breadcrumb-item.active', breadcrumb.name);
        return m('li.breadcrumb-item', [
          m('a', { href: breadcrumb.path, oncreate: m.route.link }, breadcrumb.name),
        ]);

      })),
    ]);

  }

};