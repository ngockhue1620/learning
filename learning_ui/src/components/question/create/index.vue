<template>
  <div class="exam-main">
    <div class="exam-item-left">
      <div class="exam-item-left-child-top">
        <b-card>
          <Config
            @getQuestionAction="getQuestionAction"
            @getQuestionType="getQuestionType"
        /></b-card>
      </div>
      <div class="exma-item-left-child-bottom">
        <div class="exma-item-left-child-bottom-top-button">
          <b-button variant="primary" @click="updateDataForQuestionView"
            >Hoàn Thành</b-button
          >
        </div>
        <div>
          <Editor v-model="content" />
        </div>
      </div>
    </div>
    <div class="exam-item-right">
      <QuestionView
        :question="question"
        @updateRightAnswer="updateRightAnswer"
        :createQuestion="createQuestion"
      />
    </div>
  </div>
</template>

<script>
import Config from "./Config.vue";
import QuestionView from "./QuestionView.vue";
import Editor from "@tinymce/tinymce-vue";
import questionConst from "../../../const/question";
import QuestionClass from "../../../services/question";
import { uuid } from "vue-uuid";
import questionApi from "../../../api/question";
export default {
  components: {
    Config,
    Editor,
    QuestionView,
  },
  data() {
    return {
      content: "",
      questionAction: questionConst.ACTION[0].value,
      questionType: questionConst.TYPE.SINGLE_CHOICE.value,
      question: new QuestionClass(),
    };
  },
  methods: {
    getQuestionType(value) {
      this.question.type = value;
    },
    getQuestionAction(value) {
      this.questionAction = value;
    },
    updateDataForQuestionView() {
      if (this.questionAction === questionConst.CREATE_QUESTION_CONTENT) {
        this.question.content = this.content;
      } else if (this.questionAction === questionConst.CREATE_ANSWER_CONTENT) {
        this.question.answers.push({ content: this.content, id: uuid.v1() });
      } else if (
        this.questionAction === questionConst.CREATE_DESCRIPTION_QUESTION
      ) {
        this.question.description = this.content;
      }
      this.content = "";
      console.log(this.question);
    },
    updateRightAnswer(value) {
      this.question.rightAnswer = value;
    },
    createQuestion() {
      this.question.right_answer = this.question.rightAnswer;
      questionApi.create(this.question);
    },
  },
};
</script>

<style>
</style>