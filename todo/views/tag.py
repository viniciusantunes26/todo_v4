from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo.models.task import TaskEntity
from todo.models.tag import TagEntity
from todo.serializers.tag import TagSerializer

class TagView(APIView):
  """
  List all tags or create a new tag.
  """
  def get_object(self, pk):
    try:
      return TaskEntity.objects.filter(pk=pk)
    except TaskEntity.DoesNotExist:
      return None

  def get(self, request, format=None):
    tags = TagEntity.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = TagSerializer(data=request.data)
    if (serializer.is_valid()):
      task = self.get_object(request.data.get("task"))
      if task is not None:
        serializer.save(tasks=task)
      else:
        serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  