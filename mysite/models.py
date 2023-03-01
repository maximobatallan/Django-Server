from django.db import models
from django.shortcuts import render
from django import forms
# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    
class Curso1(models.Model):
    def your_view_name(request):
        print('river')
        if request.method == 'POST':
            print('river')
            if request.post('button_clicked' == 'clicked'):
                variable = 1 
            
            else:
                variable = 2
                print('river')
        else:
            print('aca')
        return render(request,'1.html', {"variable": variable})