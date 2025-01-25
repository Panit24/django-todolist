from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodosViewSet

router = DefaultRouter()
router.register(r'todos', TodosViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
