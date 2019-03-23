from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('del/completed', views.delete_completed, name='delete_completed'),
    path('del/all', views.delete_all, name='delete_all')
]