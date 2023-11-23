export default {
    template: `<div class="p-2">
    <h4> {{resource.name}}</h4>
    <div>Creator: {{resource.creator}}</div>
    <button v-if="!resource.is_approved && role=='admin'" class="btn btn-success" @click='approveResource'> Approve </button>
    </div>`,
    props: ['resource'],
    data() {
      return {
        role: localStorage.getItem('role'),
        authToken: localStorage.getItem('auth-token'),
      }
    },
    methods: {
      async approveResource() {
        const res = await fetch(`/section/${this.resource.id}/approve`, {
          headers: {
            'Authentication-Token': this.authToken,
          },
        })
        const data = await res.json()
        if (res.ok) {
          alert(data.message)
          this.$router.go(0)
        } else {
          alert(data.message)
        }
      },
    },
  }