const m = require('mithril');

export const LoginView = {

  view: function() {

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
              name: 'password',
              type: 'text',
              placeholder: 'Email',
              autocomplete: 'off'
            }),
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
              name: 'submit',
              type: 'submit',
              value: 'Login',
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