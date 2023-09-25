from rest_framework import serializers

from todo.models.taskTag import TaskTagEntity

class TaskTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = TaskTagEntity
    fields = ['id', 'task', 'tag']