/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');


// -------------------------------------------------------------------------------------------------
// Interfaces

export interface IFABLink {
  name: string;
  route: string;
  icon: string;
}

export interface IFAB {
  buttons: Array<IFABLink>;
  mainIcon: string;
}


// -------------------------------------------------------------------------------------------------
// Component

export const FAB = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    const data = vnode.attrs.fabData as IFAB;

    return m('.fab-container', [
      m('.fab-menu', data.buttons.map((button, index) => {
        return m('.fab-menu-option', { 'data-name': button.name }, [
          m('i', { 'class': button.icon }),
        ]);
      })),
      m('.fab', [
        m('i', { 'class': data.mainIcon }),
      ]),
    ]);

  },

};

/*
<div class="fab-container">
  <div class="fab-menu">
    <div class="fab-menu-option" data-name="Home"><i class="fa fa-home"></i></div>
    <div class="fab-menu-option" data-name="Logout"><i class="fa fa-sign-out"></i></div>
  </div>
  <div class="fab"><i class="fa fa-book"></i></div>
</div>
 */