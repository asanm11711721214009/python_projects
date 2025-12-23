#flask....crud operation

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pythonsql"
    )


# CREATE
def create_student(name, mark):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO students (name, mark) VALUES (%s, %s)"
        cursor.execute(query, (name, mark))
        conn.commit()
        print("Student added successfully!")
    except Exception as e:
        print("Insert Error:", e)
    finally:
        if conn:
            conn.close()

# READ ALL
def read_students():
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    except Exception as e:
        print("Fetch Error:", e)
        return None
    finally:
        if conn:
            conn.close()

# READ BY ID
def get_student_by_id(id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
        return cursor.fetchone()
    except Exception as e:
        print("Fetch Error:", e)
        return None
    finally:
        if conn:
            conn.close()

# UPDATE
def update_student(id, mark, name):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE students SET mark=%s, name=%s WHERE id=%s"
        cursor.execute(query, (mark, name, id))
        conn.commit()
        print("Student updated successfully!")
    except Exception as e:
        print("Update Error:", e)
    finally:
        if conn:
            conn.close()

# DELETE
def delete_student(id):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE id=%s"
        cursor.execute(query, (id,))
        conn.commit()
        print("Student deleted successfully!")
    except Exception as e:
        print("Delete Error:", e)
    finally:
        if conn:
            conn.close()


#create_student('sathya',50)