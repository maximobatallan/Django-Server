from django.urls import path
from mysite import views

urlpatterns = [

    # - Homepage

    path('', views.home, name=""),
    path('bajo.html/', views.bajo,name='bajo'),
    path('medio.html/', views.medio,name='medio'),
    path('alto.html/', views.alto,name='alto'),
    path('test.html/', views.your_view_name,name='button_clicked'),
    
    
    
    #path('registrarcurso/', views.registrarCurso)


]









