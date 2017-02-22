import { isUndefined } from "util";
const m = require('mithril');

import { writerModel } from '../models/writer';
import { writerDataSingleton as wd } from '../models/singletons/writer-data';


export const LoginView = {

  oninit: () => {
    if (!isUndefined(wd.i().email)) writerModel.setEmail(wd.i().email);
    writerModel.error = null;
  },

  view: function() {

    return m('.header-cover', [
      m('.content', [
        m('.brand.fade', [
          m('h1', [
            m('span#alpha-c', '⍺'),
            'Scribbli',
          ]),
          m('small.text-danger', { style: { color: '#F96377' } }, writerModel.error),
        ]),
        m('form.login.fade-second', { onsubmit: writerModel.login }, [
          m('.input-block', [
            m('input', {
              name: 'email',
              type: 'text',
              placeholder: 'Email',
              autocomplete: 'off',
              oninput: m.withAttr('value', writerModel.setEmail),
              value: writerModel.current.email,
              style: { color: writerModel.emailPassValidation() ? '#2E3D48' : '#F96377' },
            }),
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
          ]),
          m('.input-block', [
            m('input.preauth', {
              name: 'submit',
              type: 'submit',
              value: 'Login',
              disabled: !(writerModel.emailPassValidation() && writerModel.passwordPassValidation()),
            }),
          ]),
          m('.helpful-links', [
            m('a[href="#"]', 'Forgot Password'),
            m('a[href="#"]', 'Request Access'),
          ]),
        ]),
      ]),
    ]);

  }

};