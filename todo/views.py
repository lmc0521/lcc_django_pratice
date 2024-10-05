from django.shortcuts import render
from .models import Todo
from .forms import TodoForm


# Create your views here.
def create_todo(request):
    message = ""
    form = TodoForm()

    return render(request, "todo/create-todo.html", {"form": form, "message": message})


def todo(request, id):
    user = request.user
    message = ""
    todo = None
    try:
        todo = Todo.objects.get(id=id, user=user)
    except Exception as e:
        print(e)
        message = "編號錯誤"
    return render(request, "todo/todo.html", {"todo": todo, "message": message})


def todolist(request):
    user = request.user
    todos = None
    if user.is_authenticated:
        todos = Todo.objects.filter(user=user)

    print(todos)
    return render(request, "todo/todolist.html", {"todos": todos})
