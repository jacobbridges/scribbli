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

interface FabDOMStringMap extends DOMStringMap {
  name: string;
  name_id: string;
}
interface FabHTMLElement extends HTMLElement{
  dataset: FabDOMStringMap;
}


// -------------------------------------------------------------------------------------------------
// Component

export const FAB = {

  oncreate: () => {

    let newIds: string[] = [];
    Array.prototype.forEach.call(
      document.getElementsByClassName(
        'fab-menu-option'), (el: FabHTMLElement) => {
        el.addEventListener('mouseenter', () => {
          let nel = document.createElement('span');
          nel.style.position = 'fixed';
          nel.style.right = '64px';
          nel.style.bottom = el.style.bottom;
          nel.style.lineHeight = '40px';
          nel.appendChild(document.createTextNode(el.dataset.name));
          nel.id = 'fab-menu-text-' + (newIds.length + 1);
          newIds.push(nel.id);
          el.dataset.name_id = nel.id;
          document.body.appendChild(nel);
        });
        el.addEventListener('mouseleave', () => {
          document.getElementById(el.dataset.name_id).remove();
        });
    });
    const fab = document.getElementsByClassName('fab-container');
    fab.item(0).addEventListener('mouseenter', () => {
      let count = 1;
      Array.prototype.forEach.call(
        document.getElementsByClassName(
          'fab-menu-option'), (el: HTMLElement) => {
          el.style.bottom = (count*44) + 20 + 'px';
          el.style.opacity = '1.0';
          count++;
      });
      let fabMenuEl = document
        .getElementsByClassName('fab-menu')
        .item(0) as HTMLElement;
      fabMenuEl.style.height = (count * 44) + 20 + 'px';
    }, false);
    fab.item(0).addEventListener('mouseleave', () => {
      Array.prototype.forEach.call(document.getElementsByClassName('fab-menu-option'), (el: HTMLElement) => {
        el.style.bottom = '16px';
        el.style.opacity = '0';
      });
      let fabMenuEl = document
        .getElementsByClassName('fab-menu')
        .item(0) as HTMLElement;
      fabMenuEl.style.height = '0';
      newIds = [];
    }, false);

  },

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