/// <reference path="../../interfaces/mithril.d.ts" />
const m = require('mithril');
const _ = require('lodash');

// -------------------------------------------------------------------------------------------------
// Interfaces

export interface ICalloutData {
  type?: string;
  title: string;
  content: Mithril.Vnode<any, any>;
}


// -------------------------------------------------------------------------------------------------
// Component

export const callout = {

  view: (vnode: Mithril.Vnode<any, any>) => {

    const data = vnode.attrs.calloutData as ICalloutData;
    const klass = `bs-callout bs-callout-${_.get(data,'type', 'primary')}`;

    return m('div', { class: klass }, [
      m('h4', data.title),
      data.content,
    ]);

  }

};