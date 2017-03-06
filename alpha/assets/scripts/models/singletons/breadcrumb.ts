interface Breadcrumb {
  name: string;
  path: string;
}

export class BreadcrumbModel {

  // The reference to the single instance
  private static _instance: BreadcrumbModel;

  // List of strings to build the breadcrumb with
  private _crumbs: Breadcrumb[] = [] as Breadcrumb[];

  private constructor() {
    // A private constructor "ensures" that no outside source can create a new instance
  }

  public static get Singleton() {
    return this._instance || (this._instance = new this());
  }

  /** Getters and Setters */
  public get crumbs(): Breadcrumb[] { return this._crumbs }
  public set crumbs(crumbs: Breadcrumb[]) { this._crumbs = crumbs; }

  // Add a crumb to the list of breadcrumbs
  public addCrumb(crumb: Breadcrumb): BreadcrumbModel {
    this._crumbs = [...this._crumbs, crumb];
    return BreadcrumbModel.Singleton;
  }

  // Remove a number of crumbs from the end of the list of breadcrumbs
  public removeCrumbs(number: number): BreadcrumbModel {
    this._crumbs = this._crumbs.slice(0, number);
    return BreadcrumbModel.Singleton;
  }

}