<template>
    <div v-if="therapist.id" class="profile_wrapper">
        <div class="therapist-photo">
            <img v-if="therapist.photo_url" :src="therapist.photo_url" :alt="therapist.name">
            <img v-else src="https://via.placeholder.com/400" alt="">
        </div>
        <div class="therapist-info">
            <div class="therapist-therpist_name">{{therapist.name}}</div>
            <div class="therapist-methods">
                <div class="therapist-methods_header">
                    Методы:
                </div>
                <div class="therapist-methods_list">
                    <span v-for="method in therapist.method" :key="method.id">{{method.title}}</span>
                </div>
            </div>
        </div>
    </div> 
</template>

<script>
    export default {
        name: 'Therapist',
        props: ['id'],
        data() {
            return {
                therapist: {}
            }
        },
        created() {
            this.loadTherapist()
        },
        methods: {
            async loadTherapist() {
                this.therapist = await fetch(
                    `${process.env.VUE_APP_BACKEND_HOST}/api/v0/therapist/${this.id}`
                    ).then((response) => {
                        if (response.ok) {
                            return response.json()
                        } else {
                            this.$router.push({name: '404'})
                        }
                    });
            }
        }
    }
</script>

<style scoped>
  .profile_wrapper{
    display: flex;
    justify-content: space-between;
  }
  .therapist-photo {
    flex: 0 0 40%;
  }
  .therapist-photo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .therapist-info {
      flex: 0 0 55%;
  }
  .therapist-therpist_name {
      text-transform: capitalize;
      padding: 0.5rem 0;
      background: #b7b7b7;
      font-size: 1.5rem;
      text-align: center;
  }
  .therapist-methods {
      margin-top: 1rem;
  }
  .therapist-methods_header {
      padding: 0.5rem 0;
      font-size: 1.2rem;
  }
  .therapist-methods_list {
        display: flex;
        /* justify-content: space-between; */
        margin: 0 -0.5rem;
        flex-wrap: wrap;
  }
  .therapist-methods_list span {
      background: #b7b7b7;
      margin: 0.3rem;
      padding: 0.2rem 1rem;
  }
  @media screen and (max-width: 425px) {
    .therapist-photo {
      flex: auto;
    }
    .profile_wrapper {
        flex-direction: column;
    }
  }
</style>