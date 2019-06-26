from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('<course_name>/', views.detail, name='detail'),
    path('<course_name>/students/', views.list_view_for_course, name='list_view_for_course')
]
