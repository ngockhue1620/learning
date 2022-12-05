import QUESTION from '../const/question'
class Question {
  constructor(
    content = "", description = "",
    type = QUESTION.TYPE.SINGLE_CHOICE.value,
    status = QUESTION.STATUS.DRAF,
    image = null,
    rightAnswer = null,
    createdBy = 1,
    answers = [],
    right_answer = null
  ) {
    this.description = description
    this.content = content
    this.type = type
    this.type = type
    this.status = status
    this.image = image
    this.rightAnswer = rightAnswer
    this.createdBy = createdBy
    this.answers = answers
    this.right_answer = right_answer
  }
}

export default Question