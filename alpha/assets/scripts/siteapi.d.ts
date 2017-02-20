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

  export namespace Responses {

    export interface Invitation extends Response {
      data: Model<Elements.Invitation>[];
    }

  }

  export namespace Elements {

    export interface Invitation {
      email: string;
      date_expires: string;
    }

  }

}