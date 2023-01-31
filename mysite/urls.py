from django.urls import path
from mysite import views

urlpatterns = [

    # - Homepage

    path('', views.home, name=""),
    path('registrarcurso/', views.registrarCurso)


]









