import CustomerHome from './CustomerHome.js'
import ManagerHome from './ManagerHome.js'
import AdminHome from './AdminHome.js'

export default {
  template: `<div>
  <CustomerHome v-if="userRole=='customer'"/>
  <AdminHome v-if="userRole=='admin'" />
  <ManagerHome v-if="userRole=='manager'" />
  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
    }
  },

  components: {
    CustomerHome,
    ManagerHome,
    AdminHome,
  },
}