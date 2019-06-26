from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.list_view, name='list_view'),
    path('<int:student_id>/', views.detail, name='detail')
]
