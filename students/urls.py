from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('add/', views.student_add, name='student_add'),
    path('edit/<int:student_id>/', views.student_edit, name='student_edit'),
    path('remove/<int:student_id>/', views.student_remove, name='student_remove'),
    path('', views.list_view, name='list_view'),
    path('<int:student_id>/', views.detail, name='detail')
]
