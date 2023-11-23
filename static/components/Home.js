import CustomerHome from './CustomerHome.js'
import ManagerHome from './ManagerHome.js'
import AdminHome from './AdminHome.js'
import Section from './Section.js'

export default {
  template: `<div>
  <CustomerHome v-if="userRole=='customer'"/>
  <AdminHome v-if="userRole=='admin'" />
  <ManagerHome v-if="userRole=='manager'" />
  <Section v-for="(resource, index) in resources" :key='index' :resource = "resource" />
  </div>`,

  data() {
    return {
      userRole: localStorage.getItem('role'),
      authToken: localStorage.getItem('auth-token'),
      resources: [],
    }
  },

  components: {
    CustomerHome,
    ManagerHome,
    AdminHome,
    Section,
  },
  async mounted() {
    const res = await fetch('/api/section', {
      headers: {
        'Authentication-Token': this.authToken,
      },
    })
    const data = await res.json()
    if (res.ok) {
      this.resources = data
    } else {
      alert(data.message)
    }
  },
}