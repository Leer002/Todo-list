from django.urls import path

from .views import TodoListView, TodoRemoveView

urlpatterns = [
    path('', TodoListView.as_view(), name="todo"),
    path('del/<int:pk>/', TodoRemoveView.as_view(), name="delete")
]


