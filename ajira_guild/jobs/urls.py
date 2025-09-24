from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='list'),
    path('apply/<uuid:job_id>/', views.apply_job, name='apply'),
]
