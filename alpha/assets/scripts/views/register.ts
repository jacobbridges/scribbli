const m = require('mithril');

import { invitationModel } from "../models/invitation";


export const RegisterView = {

  oninit: function(vnode: any) { invitationModel.load(decodeURIComponent(vnode.attrs.unik)) },

  view: function() {

    // If the unik string could not be matched to an invitation, show an error message
    if (invitationModel.current === null) {

      return m('.header-cover', [
        m('.content', [
          m('h2', "That can't be right.."),
          m('p.text-danger', 'This invitation does not exist.'),
        ]),
      ]);

    }

    // If the current invitation is expired, show an error message
    if (new Date() >= new Date(invitationModel.current.date_expires)) {

      return m('.header-cover', [
        m('.content', [
          m('h2', 'Expired'),
          m('p.text-danger', 'This invitation has expired.'),
        ]),
      ]);

    }

    return m('.header-cover', [
      m('.content', [
        m('.brand.fade', [
          m('h1', [
            m('span#alpha-c', '⍺'),
            'Scribbli',
          ]),
        ]),
        m('form.login.fade-second', [
          m('.input-block', [
            m('input', {
              name: 'email',
              type: 'text',
              placeholder: invitationModel.current.email,
              autocomplete: 'off',
              disabled: true,
            }),
            m('small.text-muted', 'Your email will remain private.'),
          ]),
          m('.input-block', [
            m('input', {
              name: 'pseudonym',
              type: 'text',
              placeholder: 'Pseudonym',
              autocomplete: 'off'
            }),
            m('small.text-muted', 'Your pen name -- what other writers will see.'),
          ]),
          m('.input-block', [
            m('input', {
              name: 'password',
              type: 'password',
              placeholder: 'Password',
              autocomplete: 'off'
            }),
          ]),
           m('.input-block', [
            m('input', {
              name: 'doubletap',
              type: 'password',
              placeholder: 'Verify Password',
              autocomplete: 'off'
            }),
          ]),
          m('.input-block', [
            m('input', {
              name: 'submit',
              type: 'submit',
              value: 'Register',
            }),
          ]),
        ]),
      ]),
    ]);

  }

};