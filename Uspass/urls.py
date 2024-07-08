
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.layout,name = 'home'),
    path('CREATE_USER/',views.user,name = 'user'),
    path('CREATE_PASS/',views.password, name = 'password'),
    path('RESULT/',views.result,name = 'result'),
    path('INFORMATION/',views.information,name = 'information')
]