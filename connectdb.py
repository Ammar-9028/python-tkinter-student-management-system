import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bismillah",
    database="mansoora"
)

cursor1=conn.cursor()
#cursor1.execute("CREATE DATABASE mansoora")
# cursor1.execute("SHOW DATABASES")
# for row in cursor1:
#     print(row)

# query ="CREATE TABLE Student_name  (S_roll INT AUTO_INCREMENT PRIMARY KEY, course_name VARCHAR(100) NOT NULL)"
# cursor1.execute(query)
# conn.commit()

q1='''
CREATE TABLE mansoori_students (
    S_roll INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) NOT NULL,
    email_id VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    prn VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    branch VARCHAR(50) NOT NULL,
    category VARCHAR(50),
    gender VARCHAR(10),
    year VARCHAR(10),
    semester VARCHAR(10),
    academic_year VARCHAR(20),
    percentage DECIMAL(5,2),
    photo VARCHAR(255),
    course_name VARCHAR(100) NOT NULL)
'''
#cursor1.execute(q1)


q1 = '''
INSERT INTO mansoori_students (
    student_name,
    roll_number,
    email_id,
    mobile_number,
    address,
    prn,
    date_of_birth,
    branch,
    category,
    gender,
    year,
    semester,
    academic_year,
    percentage,
    photo,
    course_name
    ) 
Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)
'''
v1=('Rahul Sharma',
    'CS101',
    'rahul@gmail.com',
    '9876543210',
    'Mumbai, Maharashtra',
    'PRN123456',
    '2003-05-15',
    'Computer Science',
    'General',
    'Male',
    '3rd',
    '6th',
    '2025-2026',
    85.50,
    'uploads/rahul.jpg',
    'B.Tech'
)


# #cursor1.execute(q1.v1)
#
# # Save changes
# #conn.commit()
#
# # 3. Show Tables
# # print("Tables in database:")
# # cursor1.execute("SHOW TABLES")
# # for table in cursor1:
# #     print(table)
#
# cursor1.execute("SELECT * FROM mansoori_students")
# for row in cursor1.fetchall():
#     print(row)
#
# cursor1.close()
# conn.close()
