import pyodbc
import random

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-K6PPOBO;'  # Replace with your server name
    'DATABASE=CMS;'  # Replace with your database name
    'Trusted_Connection=yes;' # Replace with your password
)


cursor=conn.cursor()

def insert_large_data():
    # Inserting into Department table (5 departments)

    # Inserting into Teacher table (1000 teachers)
    for i in range(1, 100):
        department_id = random.randint(1, 5)  # Assign teachers randomly to a department
        cursor.execute("INSERT INTO Teacher (TeacherID,TeacherName, DepartmentID) VALUES (?, ?)",
                       (i,f'Teacher_{i}', department_id))

    # Inserting into Student table (1000 students)
    for i in range(1, 100):
        department_id = random.randint(1, 5)  # Assign students randomly to a department
        cursor.execute("INSERT INTO Student (StudentID,StudentName, DepartmentID) VALUES (?, ?)",
                       (i,f'Student_{i}', department_id))

    # Inserting into Semester table (3 semesters)
    cursor.execute("INSERT INTO Semester (SemesterID,SemesterName, StartDate, EndDate) VALUES "
                   "(1,'Spring 2024', '2024-01-15', '2024-05-15'), "
                   "(2,'Fall 2024', '2024-08-20', '2024-12-20'), "
                   "(3,'Spring 2025', '2025-01-15', '2025-05-15');")

    # Inserting into Course table (1000 courses)
    for i in range(1, 100):
        cursor.execute("INSERT INTO Course (CourseID,CourseName) VALUES (?)",
                       (i, f'Course_{i}',))

    # Inserting into StudentCredit (STC) table (5000 entries)
    # STCID is auto-incremented, so we exclude it from the INSERT statement
    

# Insert large data into the tables
insert_large_data()

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()

print("Large data inserted successfully!")