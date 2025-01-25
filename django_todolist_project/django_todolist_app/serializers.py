from rest_framework import serializers
from .models import Todos

class TodosSerializer(serializers.ModelSerializer):
    completed = serializers.BooleanField(required=False,default=False)  
    class Meta:
        model = Todos
        fields = ['id', 'title', 'description', 'completed']
        extra_kwargs = {
            'completed': {'required': False}  # Ensure completed is optional
        }
