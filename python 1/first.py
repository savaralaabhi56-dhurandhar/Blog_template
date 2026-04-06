import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_management"
)

cursor = mydb.cursor()
cursor.execute("""
CREATE TABLE student (
    std_id INT AUTO_INCREMENT PRIMARY KEY,
    std_name VARCHAR(200),
    std_age INT,
    mobile VARCHAR(100),
    city VARCHAR(100),
    class VARCHAR(100),
    total_fee INT,
    paid_fee INT,
    balance_fee INT
);
""")

print("Table 'student' created successfully.")
