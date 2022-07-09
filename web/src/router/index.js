import { createRouter, createWebHistory } from "vue-router";
import AdminIndex from "../views/Index.vue";
import Register from "../views/Register.vue";
import Home from "../views/Home.vue"


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  mode:'hash',
  routes: [
    {
      path: "/login",
      name: "login",
      component: AdminIndex,
    },
    {
      path: "/register",
      name: "register",
      component: Register,
    },
      {
        path: "/",
        name: "index",
        redirect: "/home",
      },
      {
        path: "/home",
        name: "home",
        component: Home,
      },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.name === "login" || to.name === "register" && from.name === "login") {
    next();
  } else {
    const token = window.sessionStorage.getItem("username")

    if (!token) {
      next({ name: "login" });
    } else {
      next();
    }
  }
})


export default router;