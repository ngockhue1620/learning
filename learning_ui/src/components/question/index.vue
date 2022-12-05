<template>
  <div>
    <div>
      <button @click="showCreatedQuestions">Câu hỏi vừa tạo</button>
    </div>
    <CreateQuestion />
    <div>
      <b-modal id="question-index" title="BootstrapVue" size="xl" @show="open">
        <ListQuestion v-if="isOpen" />
      </b-modal>
    </div>
  </div>
</template>

<script>
import CreateQuestion from "./create/index.vue";
import ListQuestion from "./list/index.vue";
export default {
  components: {
    CreateQuestion,
    ListQuestion,
  },
  data() {
    return {
      isOpen: false,
    };
  },
  methods: {
    showCreatedQuestions() {
      this.$bvModal.show("question-index");
    },
    open() {
      this.isOpen = true;
    },
  },
};
</script>

<style>
</style>