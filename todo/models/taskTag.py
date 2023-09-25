from django.db import models

from .task import TaskEntity
from .tag import TagEntity

class TaskTagEntity(models.Model):
  task = models.ForeignKey(TaskEntity, on_delete=models.CASCADE)
  tag = models.ForeignKey(TagEntity, on_delete=models.CASCADE)