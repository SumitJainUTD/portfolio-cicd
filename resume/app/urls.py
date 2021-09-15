from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='sumit'),
    path('jobs', views.jobs, name='jobs'),
]