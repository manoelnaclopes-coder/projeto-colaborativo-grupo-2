"""
URL configuration for centro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [ # Caminhos das páginas
    path("admin/", admin.site.urls), # Pagina do admin
    path('', views.inicio, name="inicio"), # Página inicial
    path('aulas/', views.aula, name="aulas"), # Página de aulas
    path('pc/',views.computador, name="pc" ),
    path('progresso/', views.progresso, name="progresso"),
    path('logica/', views.logica, name="logica"),
    path('front/', views.front, name="front"),
    path('ia/', views.ia, name="ia"),
    path('hacker/', views.hacker, name="hacker"),
    path('python/', views.python, name="python"),
    path('entrar/', views.entrar, name="entrar"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('sair/', views.sair, name="sair")
    
]
