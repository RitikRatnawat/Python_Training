import sqlite3
from flask_restful import Resource, reqparse

db_location = "student_data.db"


class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help="This field cannot be left empty!")
    parser.add_argument('name')
    parser.add_argument('city')
    parser.add_argument('contact')

    @classmethod
    def find_by_id(cls, student_id):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()

        query = "SELECT * FROM Students WHERE Student_ID=?"
        result = cursor.execute(query, (student_id,))
        row = result.fetchone()
        connection.close()

        if row:
            return row

    @classmethod
    def insert_student(cls, student):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()

        query = "INSERT INTO Students VALUES(?, ?, ?, ?)"
        cursor.execute(query, (student['id'], student['name'], student['city'], student['contact']))
        connection.commit()
        connection.close()

    @classmethod
    def update_student(cls, student):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()

        query = "UPDATE Students SET Student_Name=?, City=?, Contact=? WHERE Student_ID=?"
        cursor.execute(query, (student['name'], student['city'], student['contact'], student['id']))
        connection.commit()
        connection.close()

    def get(self):
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()
        
        query = "SELECT * FROM Students"
        result = cursor.execute(query)
        
        students = []
        for row in result:
            students.append({
                'id': row[0],
                'name': row[1],
                'city': row[2],
                'contact': row[3]
            })
            
        connection.commit()
        connection.close()
        
        return {'students': students}, 200

    def post(self):
        data = Student.parser.parse_args()
        
        if Student.find_by_id(data['id']):
            return {'message': "Student with ID: {} already exists.".format(data['id'])}, 400

        student = {
            'id': data['id'],
            'name': data['name'],
            'city': data['city'],
            'contact': data['contact']
        }

        try:
            Student.insert_student(student)
        except:
            return {'message': "Error occurred during Inserting Student"}, 500

        return student, 201

    def put(self):
        data = Student.parser.parse_args()
        student = Student.find_by_id(data['id'])

        updated_student = {
            'id': data['id'],
            'name': data['name'],
            'city': data['city'],
            'contact': data['contact']
        }

        if student is None:
            try:
                Student.insert_student(updated_student)
            except:
                return {"message": "Error occurred Inserting Student"}, 500
        else:
            try:
                Student.update_student(updated_student)
            except:
                return {"message": "Error occurred Updating Student"}, 500

        return updated_student, 201

    def delete(self):
        data = Student.parser.parse_args()
        connection = sqlite3.connect(db_location)
        cursor = connection.cursor()

        query = "DELETE FROM Students WHERE Student_ID=?"
        cursor.execute(query, (data['id'],))
        connection.commit()
        connection.close()

        return {'message': 'Student Deleted'}, 201