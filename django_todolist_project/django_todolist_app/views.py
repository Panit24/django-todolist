# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Todos
from .serializers import TodosSerializer
from django.shortcuts import render, redirect
from .models import Todos
import json
from django.http import JsonResponse
from .models import Todos

def create_task(request):
  if request.method == 'POST':
      data = json.loads(request.body)
      task = Todos(title=data['title'], description=data['description'])
      task.save()
      return JsonResponse({'message': 'Task created successfully', 'task': task.to_json()}, status=201)
    
def get_all_tasks(request):
    tasks = Todos.objects.all()
    return JsonResponse({'todos': [task.to_json() for task in tasks]})
  
# Delete task
#csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        task = Todos.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=200)
      
def update_task(request, task_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        task = Todos.objects.get(id=task_id)
        task.update(set__title=data['title'], set__description=data['description'],set__completed=data['completed'])
        return JsonResponse({'message': 'Task updated successfully'})
  

    
    
    
