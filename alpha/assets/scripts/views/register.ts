const m = require('mithril');

import { invitationModel } from '../models/invitation';
import { writerModel } from '../models/writer';

const doubletapState = {
  doubletap: '',
  setDoubletap: (doubletap: string) => doubletapState.doubletap = doubletap,
  doubletapPassValidation: () => {

    return doubletapState.doubletap === writerModel.current.password;

  },
};

export const RegisterView = {

  oninit: function(vnode: any) { invitationModel.load(decodeURIComponent(vnode.attrs.unik)) },

  view: function() {

    // If the invitation has not been loaded, show an empty page
    // TODO: Add a loading animation
    if (!invitationModel.isLoaded)
      return m('');

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

    // If the current invitation has already been accepted, show an error message
    if (invitationModel.current.accepted) {

      return m('.header-cover', [
        m('.content', [
          m('h2', 'Invitation already accepted.'),
          m('p.text-danger', 'This invitation has already been accepted.'),
        ]),
      ]);

    }

    // Regardless of the form the new writer will have the email address which was associated with
    // the invitation
    writerModel.setEmail(invitationModel.current.email);
    writerModel.setUnik(invitationModel.current.unik);

    return m('.header-cover', [
      m('.content', [
        m('.brand.fade', [
          m('h1', [
            m('span#alpha-c', '⍺'),
            'Scribbli',
          ]),
        ]),
        m('form.login.fade-second', { onsubmit: writerModel.create }, [
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
              autocomplete: 'off',
              oninput: m.withAttr("value", writerModel.setName),
              value: writerModel.current.name,
              style: { color: writerModel.namePassValidation() ? '#2E3D48' : '#F96377' },
            }),
            m('small.text-muted', 'Your pen name -- what other writers will see.'),
          ]),
          m('.input-block', [
            m('input', {
              name: 'password',
              type: 'password',
              placeholder: 'Password',
              autocomplete: 'off',
              oninput: m.withAttr('value', writerModel.setPassword),
              value: writerModel.current.password,
              style: { color: writerModel.passwordPassValidation() ? '#2E3D48' : '#F96377' },
            }),
            m('small.text-muted', 'Must be at least 6 characters.')
          ]),
           m('.input-block', [
            m('input', {
              name: 'doubletap',
              type: 'password',
              placeholder: 'Verify Password',
              autocomplete: 'off',
              oninput: m.withAttr('value', doubletapState.setDoubletap),
              value: doubletapState.doubletap,
              style: { color: doubletapState.doubletapPassValidation() ? '#2E3D48' : '#F96377' },
            }),
          ]),
          m('.input-block', [
            m('input.preauth', {
              name: 'submit',
              type: 'submit',
              value: 'Register',
              disabled: !(writerModel.passValidation() && doubletapState.doubletapPassValidation()),
            }),
          ]),
        ]),
      ]),
    ]);

  }

};