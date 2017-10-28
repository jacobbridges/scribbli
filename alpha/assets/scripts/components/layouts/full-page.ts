/// <reference path="../../interfaces/mithril.d.ts" />
const m = require('mithril');


// -------------------------------------------------------------------------------------------------
// Interfaces

export interface IFullPageLayout {
  breadcrumbs: any;
  pageHeading: string;
  body: Mithril.Vnode<any, any>;
  fab: Mithril.Vnode<any, any>;
}


// -------------------------------------------------------------------------------------------------
// Component

export const FullPageLayout = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    const data = vnode.attrs.fullPageLayoutData as IFullPageLayout;

    return m('div', [
      // ▼ Breadcrumbs
      data.breadcrumbs,
      // ▲ Breadcrumbs

      // ▼ Main Content
      m('.main-content', [
        m('.container.container-mobile-fluid', [

          // ▼ Main Content Header
          m('.header.content-header', [
            m('h1', data.pageHeading)
          ]),
          // ▲ Main Content Header

          // ▼ Content
          m('.row', [
            m('.col-md-12', data.body),
          ]),
          // ▲ Content

        ]),
      ]),
      // ▲ Main Content

      // ▼ FAB
      data.fab,
      // ▲ FAB
    ]);

  }

};