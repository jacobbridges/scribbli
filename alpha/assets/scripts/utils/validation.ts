const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const pseudonymRegex = /^([A-Za-z][0-9A-Za-z_\- ]+)$/;
const worldRegex = /(^[ -\[\]-\{\}~\xB2\xB3\xB5\xC0-\xD6\xD8-\xF6\xF8-\xFF\u0141-\u0148\u014A-\u017F\u0186\u018E\u019C\u0250-\u0268\u026A\u026C\u026E-\u0270\u0274-\u0279\u0281\u0287\u028E\u029E\u0391-\u03C9 ]+$)/;


export const emailRegexCheck = (email: string): boolean => emailRegex.test(email);

export const pseudonymRegexCheck = (pseudonym: string): boolean => pseudonymRegex.test(pseudonym);

export const worldRegexCheck = (world: string): boolean => worldRegex.test(world);

export const safeHTML = (text: string): boolean => {

  return text.indexOf('<script>') === -1 && text.indexOf('<link>') === -1;

};