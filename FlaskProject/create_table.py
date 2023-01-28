import sqlite3

db_location = "student_data.db"
CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS Students(Student_ID int, Student_Name text, " \
                     "City text, Contact text)"
DELETE_TABLE_QUERY = "DROP TABLE IF EXISTS Students"


def create_table():
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()

    cursor.execute(CREATE_TABLE_QUERY)
    print("Database created successfully")

    connection.commit()
    connection.close()


def delete_table():
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()

    cursor.execute(DELETE_TABLE_QUERY)

    connection.commit()
    connection.close()

