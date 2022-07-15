from django.db import models

# Create your models here.


class Task (models.Model):     #наследование от models.Model
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title  
    
    class Meta:
        verbose_name = 'Задача'   #имя в немножественном числе 
        verbose_name_plural = 'Задачи'   #имя во множественном числе 

