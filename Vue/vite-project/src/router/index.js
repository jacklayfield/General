import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import MealList from "../views/MealList.vue";

const routes = [
  {
    path: "/",
    children: [
      {
        path: "/",
        name: "home",
        component: Home,
      },
      {
        path: "/letter/:letter",
        name: "byLetter",
        component: MealList,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
