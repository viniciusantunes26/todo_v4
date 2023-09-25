from rest_framework import serializers

from todo.models.tag import TagEntity
from todo.serializers.task import TaskSerializer

class TagSerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(many=True, required=False)

  class Meta:
    model = TagEntity
    fields = ['id', 'name', 'tasks']