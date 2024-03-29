from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('add/', views.course_add, name='course_add'),
    path('edit/<course_name>/', views.course_edit, name='course_edit'),
    path('remove/<course_name>/', views.course_remove, name='course_remove'),   
    path('<course_name>/add_lesson/', views.LessonCreateView.as_view(), name='add_lesson'),    
    path('<course_name>/', views.detail, name='detail'),
]
