

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('addTodo', views.addTodo,name="addTodo"),
    path('completeTodo/<todo_id>', views.completeTodo,name="completeTodo"),
    path('deleteCompleted', views.deleteCompleted,name="deleteCompleted"),
    path('deleteAll', views.deleteAll,name="deleteAll")
]
