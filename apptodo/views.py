from django.shortcuts import render,redirect
from . models import Todo 
from .forms import TodoForm
from django.views.decorators.http import require_POST


def index(request):
	form=TodoForm()
	todo_list=Todo.objects.order_by('id')
	context={'todo_list': todo_list,'form':form}
	return render(request,'todo/index.html',context)

@require_POST
def addTodo(request):
	form=TodoForm(request.POST)
	if form.is_valid():
		new_todo=Todo(text=request.POST['text'])
		new_todo.save()
	return redirect('index')

def completeTodo(request,todo_id):
	todo=Todo.objects.get(id=todo_id)
	todo.complete=True
	todo.save()
	return redirect("index")

def deleteCompleted(request):
	todo=Todo.objects.filter(complete__exact=True).delete()
	return redirect("index")

def deleteAll(request):
	todo=Todo.objects.all().delete()
	return redirect("index")