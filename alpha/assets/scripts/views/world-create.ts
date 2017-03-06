/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');
const BBCodeParser = require('bbcode-parser');
const parser = new BBCodeParser(BBCodeParser.defaultTags());

import { checkAuth } from '../resolvers/auth-router-resolver';
import { BreadcrumbModel } from '../models/singletons/breadcrumb';
import { breadcrumb } from '../components';
import { worldModel } from '../models/world';
import { colorTextNormal, colorTextDanger } from '../definitions';


let windowState = {
  formatting_help_display: 'none',
};

/**
 * Open a new browser window with a preview of the world description in it.
 * @param e: The onclick event.
 */
const generatePreview = (e: Event) => {

  e.preventDefault();

  let previewWindow = window.open(null, 'PreviewDescription', 'menubar=no,location=no,resizable=yes,scrollbars=yes,status=no,width=800,height=600');
  previewWindow.document.open();
  let html = `<html>
    <head>
      <title>Preview Description</title>
      <style>
        @import url('https://fonts.googleapis.com/css?family=Cabin');
        body {
          background-color: #F0F0F0;
          color: #343435;
          letter-spacing: .4px;
          font-family: 'Cabin', sans-serif;
        }
      </style>
    </head>
    <body>
      ${parser.parseString(worldModel.form.description || '')}
    </body></html>`;
  previewWindow.document.write(html);
  previewWindow.document.close();

};

/**
 * Show a help section on formatting BBCode.
 * @param e: The onclick event.
 */
const showFormattingHelp = (e: Event) => {

  e.preventDefault();

  // Toggle the help section
  windowState.formatting_help_display = document
    .getElementById('formattingHelp').style.display === 'none' ? 'block' : 'none';

};

export const worldCreateView = checkAuth({

  oninit: function() {

    BreadcrumbModel.Singleton.crumbs = [
     { name: 'Home', path: '/home' },
     { name: 'Universe', path: '/universe' },
     { name: 'Create New World', path: '/universe/new-world' },
    ];

  },

  view: function() {

    return m('div', [
      m(breadcrumb),
      m('.container', [
        m('.heading', [
          m('h1', `Create ${!Boolean(worldModel.form.name) ? 'A New World' : worldModel.form.name}`),
        ]),
      ]),
      m('.container', [
        m('.row', [
          m('.col-12.col-md-9', [
            m('form.pb-3', { onsubmit: worldModel.create }, [
              m('.text-danger.text-underline', [
                m('u', worldModel.form_errors.default
                  ? `Error: ${worldModel.form_errors.default}`
                  : ''),
              ]),
              // World Name
              m('.form-group', { 'class': worldModel.form_errors.name ? 'has-danger' : '' }, [
                m('label', { 'for': 'world-name' }, 'Name'),
                m('input#world-name.form-control', {
                  type: 'text',
                  name: 'name',
                  'aria-describedby': 'world-name-help',
                  placeholder: 'World Name Here',
                  oninput: m.withAttr('value', worldModel.setName),
                  value: worldModel.form.name,
                  style: { color: worldModel.namePassValidation() ? colorTextNormal : colorTextDanger },
                  'class': worldModel.form_errors.name ? 'form-control-danger' : '',
                }),
                m('.form-control-feedback', worldModel.form_errors.name),
              ]),
              // World Concept Art
              m('.form-group', { 'class': worldModel.form_errors.background ? 'has-danger' : '' }, [
                m('label', { 'for': 'world-concept-art' }, 'Concept Art (.jpg or .png)'),
                m('input#world-concept-art.form-control-file', {
                  type: 'file',
                  name: 'background',
                  accept: 'image/jpeg,image/png',
                  onchange: worldModel.setBackground,
                  'aria-describedby': 'world-concept-art-help',
                  'class': worldModel.form_errors.background ? 'form-control-danger' : '',
                }),
                m('.form-control-feedback', worldModel.form_errors.background),
              ]),
              // World Privacy
              m('fieldset.form-group', { 'class': worldModel.form_errors.is_public ? 'has-danger' : '' }, [
                m('div', 'Privacy'),
                m('.form-check', [
                  m('label.form-check-label', [
                    m('input#world-privacy-public.form-check-input', {
                      type: 'radio',
                      name: 'privacy',
                      value: 'public',
                      style: 'margin-right: 6px;',
                      onchange: () => worldModel.setIsPublic(true),
                      'class': worldModel.form_errors.is_public ? 'form-control-danger' : '',
                      checked: worldModel.form.is_public,
                    }),
                    m.trust('Public&mdash;this world will be listed on the Universe page. Other writers will still need your permission to create stories or destinations within this world.'),
                  ]),
                ]),
                m('.form-check', [
                  m('label.form-check-label', [
                    m('input#world-privacy-private.form-check-input', {
                      type: 'radio',
                      name: 'privacy',
                      value: 'private',
                      style: 'margin-right: 6px;' ,
                      onchange: () => worldModel.setIsPublic(false),
                      'class': worldModel.form_errors.is_public ? 'form-control-danger' : '',
                      checked: !worldModel.form.is_public,
                    }),
                    m.trust('Private&mdash;this world will be unlisted. You will need to grant "read" permission to each writer that you want to see this world.'),
                  ]),
                ]),
                m('.form-control-feedback', worldModel.form_errors.is_public),
              ]),
              // World Description
              m('.form-group', { 'class': worldModel.form_errors.description ? 'has-danger' : '' }, [
                m('label', { 'for': 'world-description' }, 'Description'),
                m('textarea#world-description.form-control', {
                  rows: 3,
                  'aria-describedby': 'world-description-help',
                  placeholder: 'Write an introduction to your new world.',
                  oninput: m.withAttr('value', worldModel.setDescription),
                  value: worldModel.form.description,
                  style: { color: worldModel.descriptionPassValidation() ? colorTextNormal : colorTextDanger },
                  'class': worldModel.form_errors.description ? 'form-control-danger' : '',
                }),
                m('small#world-description-help.form-text.text-muted', [
                  m('a.nolink', { href: '#', onclick: generatePreview }, 'Preview'),
                  m.trust(' &nbsp; '),
                  m('a.nolink', { href: '#', onclick: showFormattingHelp }, 'Formatting Help'),
                ]),
                m('.form-control-feedback', worldModel.form_errors.description),
                m('#formattingHelp', { style: { display: windowState.formatting_help_display } }, [
                  m('h5.pt-3', 'Formatting Help'),
                  m('pre', 'The following tags are currently supported: [b], [i], [u], [img], and [url].'),
                ]),
              ]),
              // World Submit
              m('button.btn.btn-primary', {
                type: 'submit',
                disabled: !worldModel.passValidation()
              }, 'Create!'),
            ]),
          ]),
        ]),
      ]),
    ]);

  },

});