from django.shortcuts import render,redirect
from .models import Curso
# - Homepage

def home(request):
    cursos = Curso.objects.all()
    return render(request, 'index.html', {"cursos": cursos})

def registrarCurso(request):
    email= request.POST['email']
    name = request.POST['name']
    creditos = request.POST['phone']
    
    curso = Curso.objects.create(nombre=email, codigo=name, creditos=creditos)
    
    return render(request,"templates/index.html",{})