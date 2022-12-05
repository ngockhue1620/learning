from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import QuestionViewSet
router = SimpleRouter()
router.register('question', QuestionViewSet, 'question')

urlpatterns = [
    path('', include(router.urls)),
]