from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LoginViewset
router = SimpleRouter()
router.register('', LoginViewset, 'user')

urlpatterns = [
    path('', include(router.urls)),
]