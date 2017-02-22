const m = require('mithril');

import { writerDataSingleton as wd } from "../models/singletons/writer-data";
import { checkAuth } from "../resolvers/auth-router-resolver";


export const homeView = checkAuth({

  view: function(vnode: Mithril.VirtualElement) {

    return m('div', [`Hello ${wd.i().name}!`, ...vnode.children]);

  }

});