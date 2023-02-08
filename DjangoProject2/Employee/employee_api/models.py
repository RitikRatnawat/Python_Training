from django.db import models


# Create your models here.
class Department(models.Model):
    department_id = models.BigAutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)


class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
