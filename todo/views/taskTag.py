from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.serializers.taskTag import TaskTagSerializer

class TaskTagView(APIView):
  """
  Associate task and tags.
  """
  def post(self, request, format=None):
    serializer = TaskTagSerializer(data=request.data)
    if (serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)