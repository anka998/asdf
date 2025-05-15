import sqlite3
con = sqlite3.connect("student.db")

class Student:
    def __init__(self, first_name, last_name, middle_name, group_num, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.group_num = group_num
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

def connect_to_db(db_name='students.db'):
    con = sqlite3.connect(db_name)
    return con

def create_table(con):
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            middle_name TEXT,
            group_num TEXT,
            grades TEXT
        )
    ''')
    con.commit()

def add_student(conn, student):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (first_name, last_name, middle_name, group_num, grades)
        VALUES (?, ?, ?, ?, ?)
    ''', (student.first_name, student.last_name, student.middle_name, student.group_num, ",".join(map(str, student.grades))))
    conn.commit()

def view_all_students(con):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for student in students:
        print(student)

def view_student(con, student_id):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
    student = cursor.fetchone()
    if student:
        grades = list(map(int, student[5].split(",")))
        avg_grade = sum(grades) / len(grades)
        print(f'Student: {student[1]} {student[2]} {student[3]}, Group: {student[4]}, Average Grade: {avg_grade}')

def edit_student(con, student_id, updated_student):
    cursor = con.cursor()
    cursor.execute('''
        UPDATE students SET first_name=?, last_name=?, middle_name=?, group_num=?, grades=?
        WHERE id=?
    ''', (updated_student.first_name, updated_student.last_name, updated_student.middle_name,
          updated_student.group_num, ",".join(map(str, updated_student.grades)), student_id))
    con.commit()

def delete_student(con, student_id):
    cursor = con.cursor()
    cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
    con.commit()

def average_grade_by_group(con, group_num):
    cursor = con.cursor()
    cursor.execute('SELECT grades FROM students WHERE group_num=?', (group_num,))
    grades_list = cursor.fetchall()
    total_grade = 0
    count = 0
    for grades in grades_list:
        grades_array = list(map(int, grades[0].split(",")))
        total_grade += sum(grades_array)
        count += len(grades_array)
    if count > 0:
        print(f'Average grade for group {group_num}: {total_grade / count}')
    else:
        print(f'No students found in group {group_num}')

con = connect_to_db()
create_table(con)

student1 = Student("Николай", "Иванов", "Сергеевич", "621", [4, 5, 3, 4])
add_student(con, student1)

student2 = Student("Павел", "Петров", "Григорьевич", "423", [5, 5, 4, 4])
add_student(con, student2)

view_all_students(con)

view_student(con, 1)

updated_student = Student("Николай", "Иванов", "Сергеевич", "621", [5, 5, 5, 5])
edit_student(con, 1, updated_student)

delete_student(con, 2)

average_grade_by_group(con, "621")

con.close()
