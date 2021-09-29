from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='aluno'),
    path('cadastro/', views.create, name='create')
]