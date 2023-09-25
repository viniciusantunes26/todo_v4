from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.category import CategoryEntity
from todo.models.task import TaskEntity
from todo.serializers.task import TaskSerializer
from todo.serializers.taskStatePercent import TaskStatePercentSerializer


class TaskDetailView(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_object(self, pk, entity):
        try:
            return entity.objects.get(pk=pk)
        except entity.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        task = self.get_object(pk, TaskEntity)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        task = self.get_object(pk, TaskEntity)
        serializer = TaskSerializer(task, data=request.data)
        if (serializer.is_valid()):
            category = self.get_object(request.data.get("category"),
                                       CategoryEntity)
            serializer.save(category=category)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        task = self.get_object(pk, TaskEntity)
        serializer = TaskStatePercentSerializer(task, data=request.data, partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        task = self.get_object(pk, TaskEntity)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    