const m = require('mithril');

import { LoginView } from "./views/login";
import { RegisterView } from "./views/register";

m.route(document.body, "/login", {
  '/login': LoginView,
  '/register/:unik': RegisterView,
});