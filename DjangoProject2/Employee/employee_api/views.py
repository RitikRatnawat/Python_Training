from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


# Create your views here.
@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_employee(request):
    emp_data = request.data
    dept_data = request.data['department']

    dept = None

    try:
        dept = Department.objects.get(department_id=dept_data['department_id'])
    except Department.DoesNotExist:
        dept = Department.objects.create(department_name=dept_data['department_name'],
                                         manager=dept_data['manager'])

    employee = Employee.objects.create(employee_name=emp_data['employee_name'],
                                       designation=emp_data['designation'],
                                       department=dept)

    employee.save()

    return Response("Employee Created Successfully")


@api_view(['GET'])
def get_departments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_department(request):
    dept = DepartmentSerializer(data=request.data)

    if dept.is_valid():
        dept.save()

    return Response("Department Created Successfully")


@api_view(['GET', 'PUT', 'DELETE'])
def employee(request, eid):
    try:
        emp = Employee.objects.get(employee_id=eid)
    except Employee.DoesNotExist:
        return Response("Employee Not Found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        emp_serializer = EmployeeSerializer(emp)
        return Response(emp_serializer.data)

    elif request.method == 'PUT':
        dept_data = request.data['department']
        dept = None

        try:
            dept = Department.objects.get(department_id=dept_data['department_id'])
            dept_serializer = DepartmentSerializer(dept, data=dept_data)

            if dept_serializer.is_valid():
                dept_serializer.save()

        except Department.DoesNotExist:
            dept = Department.objects.create(department_name=dept_data['department_name'],
                                             manager=dept_data['manager'])
            emp.department = dept

        emp_serializer = EmployeeSerializer(emp, data=request.data)

        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response("Employee Updated", status=status.HTTP_200_OK)

        return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        emp.delete()
        return Response("Employee deleted successfully", status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def department(request, dept_id):
    try:
        dept = Department.objects.get(department_id=dept_id)
    except Department.DoesNotExist:
        return Response("Department Not Found", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        dept_serializer = DepartmentSerializer(dept)
        return Response(dept_serializer.data)

    elif request.method == 'PUT':
        dept_serializer = DepartmentSerializer(dept, data=request.data)

        if dept_serializer.is_valid():
            dept_serializer.save()
            return Response("Department Updated", status=status.HTTP_200_OK)

        return Response(dept_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dept.delete()
        return Response("Department deleted successfully", status=status.HTTP_200_OK)
