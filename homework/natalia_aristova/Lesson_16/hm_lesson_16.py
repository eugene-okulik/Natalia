import mysql.connector as mysql
import os
import csv
import dotenv


dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

query = '''SELECT  DISTINCT s.name, s.second_name, g.title as 'group_title', b.title as 'book_title',
w.title as 'subject_title', l.title as 'lesson_title',  m.value as 'mark_value'
FROM students s
left join books b
on s.id = b.taken_by_student_id
left join `groups` g
on s.group_id = g.id
left join marks m
on s.id = m.student_id
left join lessons l
on m.lesson_id = l.id
left join subjets w
on l.subject_id = w.id
'''
cursor.execute(query)
data_in_db = cursor.fetchall()
db.close()

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
eugene_path = os.path.join(homework_path, 'eugene_okulik')
lesson16_path = os.path.join(eugene_path, 'Lesson_16')
hw16_path = os.path.join(lesson16_path, 'hw_data', 'data.csv')

with open(hw16_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

missed_data = []
for i in data:
    if i not in data_in_db:
        missed_data.append(i)

print(missed_data)
