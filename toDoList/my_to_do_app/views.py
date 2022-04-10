from operator import contains
from certifi import contents
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.urls import reverse

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos} # 모델이군
    return render(request, 'my_to_do_app/index.html', content) # templates 폴더 안의...

def createTodo(request):
    input_todoContent = request.POST['todoContent']
    new_todo = Todo(content=input_todoContent)
    new_todo.save() # 데이터 베이스에 알아서 저장해준다.
    # return HttpResponse('입력한 문장은 :'+ input_todoContent)
    return HttpResponseRedirect(reverse('index'))