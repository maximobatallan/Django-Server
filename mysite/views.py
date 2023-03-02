from django.shortcuts import render
from .models import Curso
from django.views.decorators.csrf import csrf_exempt

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
    
    return render(request, "alto.html")

def test(request):
    
    
    return render(request, "test.html")





@csrf_exempt
def your_view_name(request):
        resultado = 0
        respuestas = 0 
        for i in range(1, 31):
            check = str(f'checkbox{i}')
            if request.POST.get('button_clicked') == 'clicked' and request.POST.get(check):
                      
                
                bajo = 1
                medio=50
                alto=100
                
            
                if i % 3  == 1:  
                    
                    resultado = resultado + bajo
                    respuestas = respuestas + 1
                if i % 3 == 2:
                    
        
                    resultado = resultado + medio
                    respuestas = respuestas + 1
                    
                if i % 3 == 0:
                    
                    
                    resultado = resultado + alto
                    respuestas = respuestas + 1
        
 
        if respuestas !=10:
            
            
            resultado = 404
            print(respuestas)
        if respuestas == 0:
            resultado = 405
   
        else:
            resultado = resultado/10
        return render(request, 'test.html',{'variable': resultado})




