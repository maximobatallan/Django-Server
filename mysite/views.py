from django.shortcuts import render
from .models import Curso
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# - Homepage

@csrf_exempt
def home(request):

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.ambito.com/")

    element = driver.find_element(By.XPATH, value='//*[@id="mainHeader"]/div/div[3]/div/ul/li[5]/span[3]')
    element1 = driver.find_element(By.XPATH, value='//*[@id="mainHeader"]/div/div[3]/div/ul/li[2]/span[4]')
    driver.quit


    return render(request, 'index.html', {"riesgopais": element.text, "dolar": element1.text},)

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
    
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.ambito.com/")

        # Encontrar el elemento span por su etiqueta y texto de anclaje




        element = driver.find_element(By.XPATH, value='//*[@id="mainHeader"]/div/div[3]/div/ul/li[5]/span[3]')




        # Extraer el valor del elemento
        #valor = element.find_element("xpath",'//*[@id="mainHeader"]/div/div[3]/div/ul/li[5]/span[3]').text
        print(element.text)

        # Cerrar el navegador
        driver.quit()
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
        return render(request, 'test.html',{'variable': element})




