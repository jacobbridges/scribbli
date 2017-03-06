export class WriterModel {

  // The reference to the single instance
  private static _instance: WriterModel;

  // Writer's name
  private _name: string;
  // Writer's email
  private _email: string;
  // Writer's list of permission scopes
  private _scopes: string[];
  //

  private constructor() {
    // A private constructor "ensures" that no outside source can create a new instance
  }

  public static get Singleton() {
    return this._instance || (this._instance = new this());
  }

  // Just a shortcut to the singleton
  public static get i() {
    return this._instance || (this._instance = new this());
  }

  /** Getters and Setters */
  public get name(): string { return this._name; }
  public set name(name: string) { this._name = name; }
  public get email(): string { return this._email; }
  public set email(email: string) { this._email = email; }
  public get scopes(): string[] { return this._scopes; }
  public set scopes(scopes: string[]) { this._scopes = scopes; }

}