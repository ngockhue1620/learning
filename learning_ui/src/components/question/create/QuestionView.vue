<template>
  <div>
    <b-card>
      <p>Mô tả câu hỏi</p>
      <p v-html="question.description"></p>
      <p>Nội dung câu hỏi</p>
      <p v-html="question.content"></p>
      <br />
      <b-form-group label="Danh sách đáp án">
        <div
          v-for="answer in question.answers"
          :key="answer.id"
          class="answer-item"
        >
          <b-form-radio v-model="rightAnswer" :value="answer.id"></b-form-radio>
          <div v-html="answer.content" class="answer-item-content"></div>
        </div>
      </b-form-group>
    </b-card>
    <button @click="createQuestion">Tạo</button>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: [Object],
      default: () => {},
    },
    createQuestion: {
      type: [Function],
      default: () => null,
    },
  },
  data() {
    return {
      rightAnswer: null,
    };
  },
  watch: {
    rightAnswer() {
      this.$emit("updateRightAnswer", this.rightAnswer);
    },
  },
};
</script>

<style>
.answer-item {
  display: flex;
  border: 1px solid bisque;
  border-radius: 10px;
  margin: 5px;
}
.answer-item-content {
  margin-left: 20px;
}
</style>