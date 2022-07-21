from django.urls import path
from . import views

urlpatterns = [
    path('servico/', views.servico, name='servico'),
    path('',views.pdf, name='pdf'),
]

