<template>
  <div>
    <Question
      v-for="question in questions"
      :key="question.id"
      :question="question"
    />
    <Question
      v-for="question in questions"
      :key="question.id"
      :question="question"
    />
    <Question
      v-for="question in questions"
      :key="question.id"
      :question="question"
    />
  </div>
</template>

<script>
import Question from "./question.vue";
import questionApi from "../../../api/question";
export default {
  components: {
    Question,
  },
  data() {
    return {
      questions: [],
    };
  },
  methods: {
    async fetchQuestions() {
      this.questions = await questionApi.list();
      console.log(this.questions);
    },
  },
  created() {
    this.fetchQuestions();
  },
};
</script>

<style>
</style>