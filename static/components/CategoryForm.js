export default {
    template: `<div>
    <input type="text" placeholder="name" v-model="resource.name"/>
    <button @click="createResource"> Create Category</button>
    </div>`,
  
    data() {
      return {
        resource: {
          name: null,
        },
        token: localStorage.getItem('auth-token'),
      }
    },
  
    methods: {
      async createResource() {
        const res = await fetch('/api/section', {
          method: 'POST',
          headers: {
            'Authentication-Token': this.token,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.resource),
        })
  
        const data = await res.json()
        if (res.ok) {
          alert(data.message)
        }
      },
    },
  }