const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const pseudonymRegex = /^([A-Za-z][0-9A-Za-z_\- ]+)$/;

export const emailRegexCheck = (email: string): boolean => {

  return emailRegex.test(email);

};

export const pseudonymRegexCheck = (pseudonym: string): boolean => {

  return pseudonymRegex.test(pseudonym);

};