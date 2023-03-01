from django.shortcuts import render,redirect
from .models import Curso
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Curso1
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

def bajo(request):
    cursos = Curso.objects.all()
    return render(request, "bajo.html", {"cursos": cursos})

def medio(request):
    cursos = Curso.objects.all()
    return render(request, "medio.html", {"cursos": cursos})

def alto(request):
    print('river')
    return render(request, "alto.html")

def test(request):
    
    print('test')
    return render(request, "test.html")







def your_view_name(request):
    if request.method == 'POST':
        if request.POST.get('button_clicked') == 'clicked' and request.POST.get('checkbox3'):
            print('river')
            pass
        else:
            print('river2')
            # Do something else if the button is clicked but the checkbox is not checked,
            # or if the button is not clicked at all
            pass

    return render(request, 'test.html')




