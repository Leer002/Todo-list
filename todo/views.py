from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Todo
from .forms import TodoForm

class TodoListView(View):
    def get(self, request):
        todo_items = Todo.objects.all().order_by("-date")
        form = TodoForm()
        context = {"todo":todo_items, "form":form}
        return render(request, "todo/todo.html", context=context)
    
    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo")
        todo_items = Todo.objects.all().order_by("-date")
        context = {"todo":todo_items, "form":form}
        return render(request, "todo/todo.html", context=context)


class TodoRemoveView(View):
    def get(self, request, pk):
        try:
            todo_item = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            messages.error(request, "Item not found!")
        return render(request, "todo/todo.html", context={"todo":todo_item, "form":TodoForm()})
    
    def post(self, request, pk):
        try:
            todo_item = Todo.objects.get(pk=pk)
            todo_item.delete()
            messages.info(request, "Item removed!")
            return redirect("todo")
        except Todo.DoesNotExist:
            messages.error(request, "Item not found!")
        return render(request, "todo/todo.html", context={"todo":todo_item, "form":TodoForm()})
        
        