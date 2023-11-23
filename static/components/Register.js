export default{
    template:`<div>
    <h2 class="mx-2 my-2">User Signup</h2>
   <form @submit.prevent="user_signup">
     <label class="mx-2 my-2">
       Email:
       <input type="email" v-model="username" required>
     </label>
     <label class="mx-2 my-2">
       Password:
       <input type="password" v-model="password" required>
     </label>
     <button type="submit">Signup</button>
   </form>
 </div>`,
    data(){
        return{
            username:"",
            password:""
        }
    },
    methods: {
        user_signup() {
            fetch('/user/new', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    username: this.username,
                    password: this.password
                })
            })
            .then(response => response.json())
            .then(data => {
                localStorage.setItem('access_token', data.access_token);
                this.$router.push("/")
            })
						// you can also setup token in localstorage here as well to skip logging in again
            // ...
        }
    }
}