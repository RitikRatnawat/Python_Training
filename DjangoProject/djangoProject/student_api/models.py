from django.db import models


class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    student_name = models.TextField()
    city = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
