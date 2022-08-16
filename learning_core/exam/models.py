from email.policy import default
from statistics import mode
from django.db import models
from user.models import User

class TimeStampModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True



class Exam(TimeStampModel, models.Model):
  name = models.TextField()
  description = models.TextField()
  created_by = models.ForeignKey(User, related_name='exams', on_delete=models.SET_NULL, null=True)
  score = models.IntegerField()


class Category(TimeStampModel, models.Model):
  name = models.TextField()
  description = models.TextField()
  created_by = models.ForeignKey(User, related_name='categories', on_delete=models.SET_NULL, null=True)

class Question(TimeStampModel, models.Model):
  content = models.TextField()
  description = models.TextField()
  type = models.IntegerField()
  status = models.IntegerField()
  image = models.TextField()
  right_answer = models.CharField(max_length=255)
  created_by = models.ForeignKey(User, related_name='questions_of_user', on_delete=models.SET_NULL, null=True)

class QuestionCategory(TimeStampModel, models.Model):
  category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
  question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)

class ExamCategory(TimeStampModel, models.Model):
  category = models.ForeignKey(Category, related_name='categories_of_exam', on_delete=models.CASCADE)
  exam = models.ForeignKey(Question, related_name='categories_in_exam', on_delete=models.CASCADE)

class QuestionExam(TimeStampModel, models.Model):
  exam = models.ForeignKey(Exam, related_name='question_of_exam', on_delete=models.CASCADE)
  question = models.ForeignKey(Question, related_name="question_in_exam", on_delete=models.CASCADE)
  score = models.FloatField()

class Answer(models.Model):
  content = models.TextField()
  question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
  image = models.TextField()