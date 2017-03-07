export namespace SiteApi {

  export interface Response<T> {
    id: string;
    data: T;
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

    export interface WriterData {
      email: string;
      name: string;
      scopes: string[];
    }

    export interface World {
      name: string;
      slug: string;
      description: string;
      owner: string;
      universe: number;
      background_path: string;
      thumbnail_path: string;
      system: number;
      is_public: boolean;
      date_created: number;
      date_modified: number;
    }

  }

}