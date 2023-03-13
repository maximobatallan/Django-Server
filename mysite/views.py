from django.shortcuts import render
from .models import Curso
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
# - Homepage

@csrf_exempt
def home(request):


    # Insert your CoinMarketCap API key here
    api_key = '29a110c3-96df-4dc4-9617-2776200b35b2'

    # Define the URL of the API endpoint to get the BTC price
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    # Define the parameters for the API request
    parameters = {'symbol': 'BTC'}

    # Define the headers for the API request, including the API key
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}

    # Make the API request using the requests library
    response = requests.get(url, headers=headers, params=parameters)

    # Parse the response JSON to get the BTC price
    element2 = int(response.json()['data']['BTC']['quote']['USD']['price'])

    return render(request, 'index.html', {"btc":element2},)

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
        
        print(respuestas,resultado)
        if respuestas !=10 or 0:
            
            
            resultado = 404
           
   
        else: 
            
            resultado = resultado/10
        return render(request, 'test.html',{'variable': resultado})




