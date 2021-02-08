import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Therapist from '../views/Therapist'
import NotFound from '../views/NotFound'

Vue.use(VueRouter)
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/therapist/:id',
    name: 'Therapist',
    component: Therapist,
    props: true,
  },
  { 
    path: '/404', 
    name: '404',  
    component: NotFound,
  }, 
  { 
    path: '*', 
    redirect: '/404' 
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
