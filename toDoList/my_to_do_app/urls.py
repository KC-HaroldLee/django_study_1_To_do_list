# my to do app

from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # name은 별칭
    path('createTodo/', views.createTodo, name='createTodo') # 앞에 '/' 없음 
]