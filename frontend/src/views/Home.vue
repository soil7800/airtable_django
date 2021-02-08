<template>
  <div class="">
    <h1>Список терапевтов</h1>
    <div class="therapist_list">
      <router-link class="therapist_list-item_link"  v-for="therapist in therapistList" :key="therapist.id" :to="{name: 'Therapist', params: {id: therapist.id}}" append>
        <div class="therapist_list-item">
          <div class="therapist_list-item_photo">
            <img v-if="therapist.photo_url" :src="therapist.photo_url" :alt="therapist.name">
            <img v-else src="https://via.placeholder.com/100" :alt="therapist.name">
          </div>
          <div class="therapist_list-item_name">{{therapist.name}}</div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    data() {
      return {
        therapistList: []
      }
    },
    components: {},
    created() {
      this.loadTherapistList()
    },
    methods: {
      async loadTherapistList() {
        this.therapistList = await fetch(
          `${process.env.VUE_APP_BACKEND_HOST}/api/v0/therapist/`
        ).then(response => response.json()),
        console.log(this.therapistList)
      },
    }
  }
</script>

<style scoped>
  .therapist_list {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px 20px;
  }
  .therapist_list-item_link {
    text-decoration: none;
    text-transform: capitalize;
  }
  .therapist_list-item {
    height: 100%;
    display: flex;
    flex-direction: column;
    background: #f6f7f9;
    padding: 1rem 1rem;
    text-align: center;
    box-shadow: 0 .2rem 1rem rgba(0,0,0,.15);
  }
  .therapist_list-item_photo {
    margin-bottom: 1rem;
  }
  .therapist_list-item_photo img{
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
  }
  .therapist_list-item_name {
    height: 100%;
  }
  @media screen and (max-width: 780px) {
    .therapist_list {
      grid-template-columns: repeat(4, 1fr)
    }
  }
  @media screen and (max-width: 620px) {
    .therapist_list {
      grid-template-columns: repeat(3, 1fr)
    }
  }
  @media screen and (max-width: 470px) {
    .therapist_list {
      grid-template-columns: repeat(2, 1fr)
    }
  }

</style>