from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('add/', views.StudentCreateView.as_view(), name='student_add'),
    path('edit/<pk>/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('remove/<pk>/', views.StudentDeleteView.as_view(), name='student_remove'),
    path('', views.StudentListView.as_view(), name='list_view'),
    path('<pk>/', views.StudentDetailView.as_view(), name='detail')
]
