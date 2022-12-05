
export default {
  TYPE: {
    SINGLE_CHOICE: { name: "Câu hỏi 1 lựa chọn", value: 1 },
    MULTIPLE_CHOICE: { name: "Câu hỏi nhiều lựa chọn", value: 2 }
  },
  ACTION: [
    { name: "Tạo nội dung câu hỏi", value: 1 },
    { name: "Tạo nội dung đáp án", value: 2 },
    { name: "Mô tả câu hỏi", value: 3 },
  ],
  STATUS: {
    PUBLISHED: 1,
    DRAF: 2
  },
  CREATE_QUESTION_CONTENT: 1,
  CREATE_ANSWER_CONTENT: 2,
  CREATE_DESCRIPTION_QUESTION: 3
}