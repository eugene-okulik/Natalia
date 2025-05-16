import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
query_student = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Natasha', 'Aristova')
cursor.execute(query_student, values)
db.commit()
student_id = cursor.lastrowid

query_books = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values_books = [
    ('War and Piece', student_id),
    ('Idiot', student_id),
    ('One flew over the cuckoos nest', student_id)
]
cursor.executemany(query_books, values_books)
db.commit()

query_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
value_group = ('AQA1', 'march 2025', 'may 2067')
cursor.execute(query_group, value_group)
db.commit()
group_id = cursor.lastrowid
cursor.execute(f'UPDATE students SET group_id = {group_id} WHERE id = {student_id}')
db.commit()

query_subjects = 'INSERT INTO subjets (title) VALUES (%s)'
value_sub_1 = ['English_beginner']
cursor.execute(query_subjects, value_sub_1)
db.commit()
sub1_id = cursor.lastrowid
value_sub_2 = ['Deutsch']
cursor.execute(query_subjects, value_sub_2)
db.commit()
sub2_id = cursor.lastrowid

query_lessons = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values_lessons_1 = ['beginner_1', sub1_id]
cursor.execute(query_lessons, values_lessons_1)
db.commit()
les1_id = cursor.lastrowid
values_lessons_2 = ['beginner_2', sub1_id]
cursor.execute(query_lessons, values_lessons_2)
db.commit()
les2_id = cursor.lastrowid
values_lessons_3 = ['deutsch_1', sub2_id]
cursor.execute(query_lessons, values_lessons_3)
db.commit()
les3_id = cursor.lastrowid
values_lessons_4 = ['deutsch_2', sub2_id]
cursor.execute(query_lessons, values_lessons_4)
db.commit()
les4_id = cursor.lastrowid

query_marks = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
values_marks = [
    (5, les1_id, student_id),
    (4, les2_id, student_id),
    (5, les3_id, student_id),
    (5, les4_id, student_id)
]
cursor.executemany(query_marks, values_marks)
db.commit()
final_query = '''SELECT 
s.name AS "Student name", 
s.second_name AS "Student last name", 
g.title AS "Group name", 
m.value AS "Mark", 
GROUP_CONCAT(b.title) AS "Book title", 
l.title AS "Lesson", 
w.title AS "Subject"
FROM 
students s 
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets w ON l.subject_id = w.id
WHERE 
s.id = %s
GROUP BY 
s.id, s.name, s.second_name, g.title, m.value, l.title, w.title;
'''
cursor.execute(final_query, (student_id, ))
print(cursor.fetchall())
db.commit()
db.close()
