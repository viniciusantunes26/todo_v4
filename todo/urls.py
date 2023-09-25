from django.urls import path
from todo.views.category import CategoryView
from todo.views.categoryDetail import CategoryDetailView
from todo.views.categoryTask import CategoryTaskView
from todo.views.task import TaskView
from todo.views.taskDetail import TaskDetailView
from todo.views.tag import TagView
from todo.views.taskTag import TaskTagView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('categories/<int:pk>/tasks/', CategoryTaskView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('task_tags/', TaskTagView.as_view()),
]
