from rest_framework import serializers
from todo.models.task import TaskEntity

class TaskStatePercentSerializer(serializers.ModelSerializer):
   class Meta:
        model = TaskEntity
        fields = ['id', 'percent', 'state']