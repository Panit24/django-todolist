from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Todos
from .serializers import TodosSerializer

class TodosViewSet(ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer