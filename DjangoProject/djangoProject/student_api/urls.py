from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:sid>', views.individual_student)
]
