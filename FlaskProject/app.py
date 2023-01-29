from flask import Flask, render_template, request
from flask_restful import Api
from student import Student
from create_table import create_table
import requests
import json

create_table()
app = Flask(__name__)
api = Api(app)
api_url = "http://127.0.0.1:5000/students"

api.add_resource(Student, '/students')

@app.route("/", methods=["GET", "POST"])
def render():
    if request.method == "POST":
        btn_pressed = request.form['pressed']
        
        if btn_pressed == "Add Student":
            student = {
                "id": request.form['id'],
                "name": request.form['name'],
                "city": request.form['city'],
                "contact": request.form['contact'],
            }
            
            response = requests.post(api_url, json=student)
            # print(response.text)
            
        if btn_pressed == "Update Student":
            student = {
                "id": request.form['id'],
                "name": request.form['name'],
                "city": request.form['city'],
                "contact": request.form['contact'],
            }
            
            response = requests.put(api_url, json=student)
            # print(response.text)
            
        if btn_pressed == "Delete Student":
            student = {
                "id": request.form['id']
            }
            
            response = requests.delete(api_url, json=student)
            # print(response.text)
    
    response = requests.get(api_url)
    data = response.text
    data = json.loads(data)
    # print(data)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
