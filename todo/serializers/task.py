from rest_framework import serializers

from todo.models.task import TaskEntity
from todo.models.tag import TagEntity

class TaskSerializer(serializers.ModelSerializer):
   category = serializers.SlugRelatedField(
       read_only = True,
       slug_field = 'name'
   )
   
   tags = serializers.SlugRelatedField(
       queryset=TagEntity.objects.all(),
       many = True,
       slug_field = 'name'
   )

   class Meta:
        model = TaskEntity
        fields = ['id', 'name', 'category', 'description', 'percent', 'state', 'tags']