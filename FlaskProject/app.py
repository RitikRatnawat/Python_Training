from flask import Flask
from flask_restful import Api
from student import Student
from create_table import create_table

create_table()
app = Flask(__name__)
api = Api(app)

api.add_resource(Student, '/student/<int:student_id>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
