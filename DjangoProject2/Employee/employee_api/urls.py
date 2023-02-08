from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("employees/", views.get_employees),
    path("departments/", views.get_departments),
    path("create-employee/", views.create_employee),
    path("create-department/", views.create_department),
    path("employee/<int:eid>", views.employee),
    path("department/<int:dept_id>", views.department),
]
