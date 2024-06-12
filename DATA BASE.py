import sqlite3

# Создание базы данных и таблиц
conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject TEXT,
        grade REAL,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
''')

conn.commit()


class University:
    def __init__(self, name):
        self.name = name

    def add_student(self, name, age):
        cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        conn.commit()

    def add_grade(self, student_id, subject, grade):
        cur.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", (student_id, subject, grade))
        conn.commit()

    def get_students(self, subject=None):
        if subject:
            cur.execute("SELECT students.name, students.age, grades.subject, grades.grade FROM students JOIN grades ON students.id = grades.student_id WHERE grades.subject = ?", (subject,))
        else:
            cur.execute("SELECT students.name, students.age, grades.subject, grades.grade FROM students JOIN grades ON students.id = grades.student_id")
        result = cur.fetchall()
        return result


# Пример использования
u1 = University('Urban')

u1.add_student('Ivan', 26)  # id - 1
u1.add_student('Ilya', 24)  # id - 2

u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)

print(u1.get_students())
print(u1.get_students('Python'))

# Закрываем соединение с базой данных
conn.close()
