const m = require('mithril');

import { LoginView } from "./views/login";

m.route(document.body, "/login", {
  '/login': LoginView,
});