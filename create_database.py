import sqlite3

connection = sqlite3.connect("student_database.db")
cursor = connection.cursor()

print("Database connection successful!")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        department TEXT NOT NULL,
        level TEXT NOT NULL,
        attendance_average REAL,
        average_exam_score REAL
    )
""")

# Student records
students = [
    ("CUL/CS/001", "Computer Science", "100L", 92.5, 78.0),
    ("CUL/CS/002", "Computer Science", "200L", 85.0, 81.5),
    ("CUL/CS/003", "Computer Science", "300L", 90.0, 88.0),
    ("CUL/SE/004", "Software Engineering", "200L", 87.5, 75.0),
    ("CUL/SE/005", "Software Engineering", "300L", 91.0, 86.5),
    ("CUL/CY/006", "Cybersecurity", "100L", 80.0, 72.5),
    ("CUL/CY/007", "Cybersecurity", "200L", 89.5, 90.0),
    ("CUL/IT/008", "Information Technology", "300L", 94.0, 83.5),
    ("CUL/IT/009", "Information Technology", "400L", 96.0, 88.5),
    ("CUL/CS/010", "Computer Science", "400L", 78.5, 69.0)
]

# Insert records into the database
cursor.executemany("""
    INSERT OR IGNORE INTO students
    (student_id, department, level, attendance_average, average_exam_score)
    VALUES (?, ?, ?, ?, ?)
""", students)

print("Student records inserted successfully!")

connection.commit()
# Retrieve student records
cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

# Display student records
print("\nSTUDENT DATABASE")
print("-" * 90)

for record in records:
    student_id, department, level, attendance, exam_score = record

    print(f"""
Student ID: {student_id}
Department: {department}
Level: {level}
Attendance Average: {attendance}%
Average Examination Score: {exam_score}%
""")

print("-" * 90)
print(f"Total students: {len(records)}")

print("Students table created successfully!")
connection.close()