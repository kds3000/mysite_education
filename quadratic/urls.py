from django.urls import path, re_path
from . import views

app_name = 'quadratic'

    
urlpatterns = [
    re_path(r'^results/$', views.quadratic_equation_solutions, name = 'results'),
]

