from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Jobs, name="jobs_list"),
    path('search', views.search, name="search"),
    path('<int:i_id>', views.detail, name='detail'),
    path('apply/<int:job_id>', views.apply, name='apply'),
    path('applications', views.applications, name='applications'),
    path('applications/<int:application_id>', views.application_detail, name='application_detail')
    ]