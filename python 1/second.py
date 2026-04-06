import mysql.connector

# ---------------------------
# Create MySQL connection
# ---------------------------
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # your MySQL username
            password="",       # your MySQL password
            database="student_management"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# ---------------------------
# Add a new student
# ---------------------------
def add_student(name, age, mobile, city, cls, total_fee, paid_fee, balance_fee):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = """INSERT INTO student
                 (std_name, std_age, mobile, city, class, total_fee, paid_fee, balance_fee)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, age, mobile, city, cls, total_fee, paid_fee, balance_fee)
        cursor.execute(sql, values)
        connection.commit()
        print("Student added successfully.")
        cursor.close()
        connection.close()

# ---------------------------
# View all students
# ---------------------------
def view_students():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Mobile: {row[3]}, City: {row[4]}, Class: {row[5]}, Total Fee: {row[6]}, Paid Fee: {row[7]}, Balance: {row[8]}")
        cursor.close()
        connection.close()

# ---------------------------
# Update student by ID
# ---------------------------
def update_student(std_id, name, age, mobile, city, cls, total_fee, paid_fee, balance_fee):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = """UPDATE student
                 SET std_name=%s, std_age=%s, mobile=%s, city=%s, class=%s,
                     total_fee=%s, paid_fee=%s, balance_fee=%s
                 WHERE std_id=%s"""
        values = (name, age, mobile, city, cls, total_fee, paid_fee, balance_fee, std_id)
        cursor.execute(sql, values)
        connection.commit()
        print("Student updated successfully.")
        cursor.close()
        connection.close()

# ---------------------------
# Delete student by ID
# ---------------------------
def delete_student(std_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM student WHERE std_id=%s"
        cursor.execute(sql, (std_id,))
        connection.commit()
        print("Student deleted successfully.")
        cursor.close()
        connection.close()

# ---------------------------
# Main menu
# ---------------------------
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            mobile = input("Mobile: ")
            city = input("City: ")
            cls = input("Class: ")
            total_fee = int(input("Total Fee: "))
            paid_fee = int(input("Paid Fee: "))
            balance_fee = int(input("Balance Fee: "))
            add_student(name, age, mobile, city, cls, total_fee, paid_fee, balance_fee)

        elif choice == "2":
            view_students()

        elif choice == "3":
            std_id = int(input("Student ID to update: "))
            name = input("Name: ")
            age = int(input("Age: "))
            mobile = input("Mobile: ")
            city = input("City: ")
            cls = input("Class: ")
            total_fee = int(input("Total Fee: "))
            paid_fee = int(input("Paid Fee: "))
            balance_fee = int(input("Balance Fee: "))
            update_student(std_id, name, age, mobile, city, cls, total_fee, paid_fee, balance_fee)

        elif choice == "4":
            std_id = int(input("Student ID to delete: "))
            delete_student(std_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

# ---------------------------
# Run the main menu
# ---------------------------
if __name__ == "__main__":
    main()
