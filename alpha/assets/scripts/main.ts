/// <reference path="./interfaces/mithril.d.ts" />
const m = require('mithril');

import { LoginView } from './views/login';
import { RegisterView } from './views/register';
import { homeView } from './views/home';
import { universeView } from './views/universe';
import { worldCreateView } from './views/world-create';

m.route(document.body, "/login", {
  '/login': LoginView,
  '/register/:unik': RegisterView,
  '/home': homeView,
  '/universe': universeView,
  '/universe/new-world': worldCreateView,
});