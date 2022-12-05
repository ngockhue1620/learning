<template>
  <b-card class="question-item">
    <strong v-html="question.description"></strong>
    <p v-html="question.content"></p>
    <div
      v-for="answer in question.answers"
      :key="answer.id"
      class="answer-item"
    >
      <b-form-radio></b-form-radio>
      <div v-html="answer.content" class="answer-item-content"></div>
    </div>
  </b-card>
</template>

<script>
export default {
  props: {
    question: {
      type: [Object],
      default: () => {},
    },
  },
};
</script>

<style>
.question-item {
  margin: 5px;
}
</style>