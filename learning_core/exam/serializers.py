from rest_framework import serializers
from .models import Answer, Exam, Question

class ExamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Exam
    fields = '__all__'

class AnsswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = '__all__'    
    extra_kwargs = {'question': {'read_only': True}}

class QuestionSerializer(serializers.ModelSerializer):
  answers = AnsswerSerializer(many=True, required = True)
  class Meta:
    model = Question
    fields = [
      'content',
      'description',
      'type',
      'status',
      'image',
      'right_answer',
      'created_by',
      'answers'
    ]
  
  def create(self, validated_data):
    answers = validated_data.pop("answers")
    question = Question.objects.create(**validated_data)
    answer_objects = []
    for answer in answers:
      answer_objects.append(Answer(**answer, question = question))
    Answer.objects.bulk_create(answer_objects)
    return question
