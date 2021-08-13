<template>
  <section class="section is-small">
    <div class="hero">
      <div class="hero-body">
        <p class="title">Promote your event</p>
        <p class="subtitle">What is your event all about?</p>
      </div>
    </div>
    <form class="container is-max-desktop">
      <input
        class="input block"
        type="text"
        placeholder="What is the event called?"
        id="title"
      />
      <label for="start_time" class="block">
        <h3>When does the event start?</h3>
        <input class="input" type="datetime-local" id="start_time" />
      </label>
      <label for="end_time" class="block">
        <h3>When does the event end?</h3>
        <input class="input" type="datetime-local" id="end_time" />
      </label>

      <input
        class="input block"
        type="text"
        placeholder="Tell us more about your event"
        id="content"
      />
      <button @click="submit">
        Submit event
      </button>
    </form>
  </section>
</template>
<script>
// TODO: send the response
export default {
  name: "Promote",
  data() {
    return {
      loading: true,
    };
  },
  methods: {
    submit: function () {
      this.errors = {};
      const url = "http://localhost:5000/events/";
      const options = {
        mehtod: "POST",
        body: this.$refs.form,
        headers: {
          "Content-Type": "application/json",
        },
      };
      fetch(url, options)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error("Failed post");
          console.error(error);
          this.errors.push(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>
