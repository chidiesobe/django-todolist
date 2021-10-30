from django.urls import path
from . import views 


urlpatterns = [
    path('',views.homepage, name = 'homepage'),
    path('createtodo',views.create, name="createTodo"),
    path('completetodo',views.completed, name="completeTodo"),
    path('update/<int:todo_id>', views.update, name = 'updateTodo')
]