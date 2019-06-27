from django.urls import path
from . import views

app_name = 'coaches'

urlpatterns = [
    path('<coach_name>/', views.detail, name='detail')
]
