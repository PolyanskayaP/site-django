from django.urls import path
from . import views    #из этой . папки импорт вьюс 

urlpatterns = [
    path('', views.index, name ='home'),       #при переходе на глав стр вызывается функция индекс из файла вьюс (сами создали)
    path('about', views.about, name='about')  #name сами прописали 
]