from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from .forms import CreateTodo

def index(request):
    items = Todo.objects.all()
    if request.method == 'POST':
        form = CreateTodo(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/')
    elif request.method == 'GET':
        form = CreateTodo()
    else:
        form = CreateTodo()
    context = {
        'items':items,
        'form':form,
        }
    return render(request, 'index.html', context)

def delete_todo(request, id):
    item = get_object_or_404(Todo, pk=id)
    item.delete()
    return redirect('/')