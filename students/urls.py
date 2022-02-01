from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_homepage, name='student_homepage'),
    path('login', views.student_login, name='student_login'),
    path('register', views.student_register, name='student_register')
]