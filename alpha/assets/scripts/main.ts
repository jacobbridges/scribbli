const m = require('mithril');

import { LoginView } from "./views/login";
import { RegisterView } from "./views/register";
import { homeView } from "./views/home";

m.route(document.body, "/login", {
  '/login': LoginView,
  '/register/:unik': RegisterView,
  '/home': homeView,
});