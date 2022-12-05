from pydoc import visiblename
from rest_framework import viewsets

from .serializers import ExamSerializer, QuestionSerializer
from .models import Exam, Question

class ExamViewSet(viewsets.ModelViewSet):
  queryset= Exam.objects.all()
  serializer_class = ExamSerializer

class QuestionViewSet(viewsets.ModelViewSet):
  queryset= Question.objects.all()
  serializer_class = QuestionSerializer
