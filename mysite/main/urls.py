from django.urls import path
from . import views    #из этой . папки импорт вьюс 

urlpatterns = [
    path('', views.index),       #при переходе на глав стр вызывается функция индекс из файла вьюс (сами создали)
    path('about-us', views.about)
]