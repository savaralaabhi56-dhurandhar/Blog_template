import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_management"
)

cursor = mydb.cursor()

cursor.execute("""
CREATE TABLE employee (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(200),
    emp_age INT,
    mobile VARCHAR(100),
    city VARCHAR(100),
    department VARCHAR(100),
    salary INT,
    bonus INT,
    total_salary INT
);
""")

print("Table 'employee' created successfully.")
