export namespace SiteApi {

  export interface Response {
    id: string;
    data: any;
  }

  export interface Model<T> {
    model: string;
    pk: string;
    fields: T;
  }

  interface DataError {
    message: string;
    extra?: any;
  }
  export interface ErrorResponse {
    id: string;
    data: DataError;
  }

  export namespace Responses {

    export interface LoadInvitation extends Response {
      data: Model<Elements.Invitation>[];
    }

    export interface CreateWriter extends Response {
      data: Model<Elements.Writer>[];
    }

  }

  export namespace Elements {

    export interface Invitation {
      email: string;
      date_expires: string;
      accepted: boolean;
      unik: string;
    }

    export interface Writer {
      email: string;
      name: string;
      date_created: string;
    }

  }

}