class Student:
    def __init__(self, surname, date, group_num, grades):
        self.surname = surname
        self.date = date
        self.group_num = group_num
        self.grades = grades

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_date(self, new_date):
        self.date = new_date

    def change_group_num(self, new_group_num):
        self.group_num = new_group_num

    def info(self):
        return f'Фамилия: {self.surname}, Дата рождения: {self.date}, ' \
            f'Номер группы: {self.group_num}, Успеваемость: {self.grades}'

surname_to_search = input("Введите фамилию студента: ")

students = [
        Student("Иванов", "15.09.2004", "823", [5, 4, 3, 5, 4]),
        Student("Петров", "07.03.2007", "932", [4, 3, 4, 3, 5]),
        Student("Сидоров", "28.11.2006", "844-k", [3, 5, 4, 4, 5])
]
students[0].change_surname("Сергеев")
students[1].change_date("22.08.2005")
students[2].change_group_num("712")

found_student = None
for student in students:
    if student.surname == surname_to_search:
        found_student = student
        break

if found_student:
    print(found_student.info())
else:
    print("Студент не найден.")
