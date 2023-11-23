import Home from './components/Home.js'
import Login from './components/Login.js'
import Users from './components/Users.js'
import CategoryForm from './components/CategoryForm.js'
import Register from './components/Register.js'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/users', component: Users },
  { path: '/create-category', component: CategoryForm },
  // { path: '/register', component: Register, name: 'Register' },
]

export default new VueRouter({
  routes,
})