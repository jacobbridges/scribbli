/// <reference path="../interfaces/mithril.d.ts" />
const m = require('mithril');
const Cookies = require('js-cookie');
import { get, map } from 'lodash';

import { worldRegexCheck,safeHTML } from '../utils/validation';
import { WriterModel as wd } from './singletons/writer-data';
import { SiteApi } from '../siteapi';


// -------------------------------------------------------------------------------------------------
// Interfaces

interface WorldForm {
  name: string;
  description: string;
  universe: number;
  background: File;
  // system: number;  TODO: Add select box for system
  is_public: boolean;
}


// -------------------------------------------------------------------------------------------------
// Model

export const worldModel = {

  // The current world
  current: {} as SiteApi.Elements.World,

  // Form errors
  form_errors: {
    'default': [] as string[],
    name: [] as string[],
    description: [] as string[],
    background: [] as string[],
    system: [] as string[],
    is_public: [] as string[],
    clear: () => {
      worldModel.form_errors.default = [];
      worldModel.form_errors.name = [];
      worldModel.form_errors.description = [];
      worldModel.form_errors.background = [];
      worldModel.form_errors.system = [];
      worldModel.form_errors.is_public = [];
    }
  },

  // The world being created (in the world create form)
  form: {} as WorldForm,

  // Setters
  setName: (name: string) => worldModel.form.name = name,
  setDescription: (description: string) => worldModel.form.description = description,
  setIsPublic: (is_public: boolean) => worldModel.form.is_public = is_public,

  // Special setter for background (because files are bitches)
  setBackground: (e: any) => worldModel.form.background = e.target.files[0],

  // Validation
  namePassValidation: () => typeof(worldModel.form.name) === 'string'
    && worldRegexCheck(worldModel.form.name)
    && worldModel.form.name.length <= 40,
  descriptionPassValidation: () => typeof(worldModel.form.description) === 'string'
    && safeHTML(worldModel.form.description),
  passValidation: () => worldModel.namePassValidation()
    && worldModel.descriptionPassValidation()
    && worldModel.form.background !== undefined,

  // Create a new world via siteapi
  create: (e: Event) => {

    // Prevent the form from submitting naturally
    e.preventDefault();

    // Wipe the form errors
    worldModel.form_errors.clear();

    // Create an empty FormData container
    let formData = new FormData();

    // Add the form's data to the FormData container
    formData.append('name', worldModel.form.name);
    formData.append('description', worldModel.form.description);
    formData.append('is_public', worldModel.form.is_public);
    formData.append('background', worldModel.form.background);
    formData.append('universe', 1);

    // Get the CSRF token from the cookie
    const csrfToken = Cookies.get('csrftoken');

    // Create the siteapi request
    return m.request({
      method: 'POST',
      url: '/api/world/',
      headers: { 'X-CSRFToken': csrfToken },
      data: formData,
    }).then((apiResponse: SiteApi.Response<any>) => {

      if (apiResponse.id === 'success') {

        let successResponse = apiResponse as SiteApi.Response<SiteApi.Elements.World>;

        // Set the API response to the current world object
        worldModel.current = successResponse.data;

        // Route to the newly created world
        worldModel.form = {} as WorldForm;
        // m.route.set(`/universe/world/${worldModel.current.slug}`);

      } else if (apiResponse.id === 'failure') {

        let errorResponse = apiResponse as SiteApi.ErrorResponse;

        // Copy errors from the response into the form
        worldModel.form_errors.name = worldModel.form_errors.name
          .concat(<string[]>map(get(errorResponse, 'data.extra.name', []), 'message'));
        worldModel.form_errors.description = worldModel.form_errors.description
          .concat(<string[]>map(get(errorResponse, 'data.extra.description', []), 'message'));
        worldModel.form_errors.background = worldModel.form_errors.background
          .concat(<string[]>map(get(errorResponse, 'data.extra.background', []), 'message'));
        worldModel.form_errors.system = worldModel.form_errors.system
          .concat(<string[]>map(get(errorResponse, 'data.extra.system', []), 'message'));
        worldModel.form_errors.is_public = worldModel.form_errors.is_public
          .concat(<string[]>map(get(errorResponse, 'data.extra.is_public', []), 'message'));

        // Check if the "__all__" key is set in the response, which signals an error with the
        // general form and not with a specific field
        if (get(errorResponse, 'data.extra.__all__', null) !== null) {

          worldModel.form_errors.default = worldModel.form_errors.default
            .concat(<string[]>get(errorResponse, 'data.extra.__all__', []));

        }

        // If the error "World with this Name and Universe already exists." is in the list of all
        // errors, add a better error  to the name field.
        if (worldModel.form_errors.default.indexOf('World with this Name and Universe already exists.') >= 0) {

          worldModel.form_errors.name.push('A world with a similar name already exists.');

        }

        document.querySelector('form').scrollIntoView();

      }

    });

  }

};