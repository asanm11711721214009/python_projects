from flask import Flask, render_template, request, redirect
from crud_operations_mysql.crud_students import *

app = Flask(__name__)
# ---------------------------------------------------
# ROUTES
# ---------------------------------------------------

@app.route('/')
def home():
    students = read_students()

    return render_template('index.html', students=students)


@app.route('/add')
def add_page():
    return render_template('add.html')


@app.route('/add_student', methods=['POST'])
def add_student_route():
    name = request.form['name']
    mark = request.form['mark']
    create_student(name, mark)
    return redirect('/')


@app.route('/edit/<int:id>')
def edit_page(id):
    student = get_student_by_id(id)
    print(student)
    return render_template('edit.html', student=student)


@app.route('/update/<int:id>', methods=['POST'])
def update_student_route(id):
    id = request.form['id']
    name = request.form['name']
    mark = request.form['mark']
    update_student(id, mark, name)
    return redirect('/')                #redirect to home page


@app.route('/delete/<int:id>')
def delete_student_route(id):
    delete_student(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)