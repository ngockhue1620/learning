<template>
  <div>
    <p>Chọn Loại câu hỏi</p>
    <b-form-select
      v-model="selectedType"
      :options="questionType"
      class="mb-3"
      value-field="value"
      text-field="name"
    ></b-form-select>
    <b-form-select
      v-model="selectedAction"
      :options="questionAction"
      class="mb-3"
      value-field="value"
      text-field="name"
    ></b-form-select>
  </div>
</template>

<script>
import question from "../../../const/question";
export default {
  data() {
    return {
      selectedType: question.TYPE.SINGLE_CHOICE.value,
      questionType: [],
      selectedAction: question.ACTION[0].value,
      questionAction: question.ACTION,
    };
  },
  watch: {
    selectedType() {
      this.$emit("getQuestionType", this.selectedType);
    },
    selectedAction() {
      this.$emit("getQuestionAction", this.selectedAction);
    },
  },
  methods: {
    buildListQuestionType() {
      let questionType = Object(question.TYPE);
      let result = [];
      for (let type in questionType) {
        result.push(questionType[type]);
      }
      return result;
    },
  },
  created() {
    this.questionType = this.buildListQuestionType();
  },
};
</script>

<style>
</style>