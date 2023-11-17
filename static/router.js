import Home from './components/Home.js'
import Login from './components/Login.js'
import Users from './components/Users.js'
import CategoryForm from './components/CategoryForm.js'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/users', component: Users },
  { path: '/create-resource', component: CategoryForm },
]

export default new VueRouter({
  routes,
})