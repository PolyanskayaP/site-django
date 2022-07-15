from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

#from django.http import HttpResponse
# Create your views here.


def index(request):
    tasks = Task.objects.order_by('-id')    #.all [:5] срез
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})   #реквест, хтмл-шаблон, словарь(ключЗначение) 


def about(request):
    return render(request, 'main/about.html')
#return HttpResponse("<h4>About</h4>")

def create(request):
    error = ''  
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)   #, context
