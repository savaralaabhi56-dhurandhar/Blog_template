import mysql.connector

# ---------------------------
# Create MySQL connection
# ---------------------------
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="employee_management"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# ---------------------------
# Add a new employee
# ---------------------------
def add_employee(name, age, mobile, city, dept, salary, bonus, total_salary):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        sql = """INSERT INTO employee
                 (emp_name, emp_age, mobile, city, department, salary, bonus, total_salary)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

        values = (name, age, mobile, city, dept, salary, bonus, total_salary)

        cursor.execute(sql, values)
        connection.commit()

        print("Employee added successfully.")

        cursor.close()
        connection.close()


# ---------------------------
# View employees
# ---------------------------
def view_employees():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employee")

        rows = cursor.fetchall()

        for row in rows:
            print(f"ID:{row[0]}, Name:{row[1]}, Age:{row[2]}, Mobile:{row[3]}, City:{row[4]}, Department:{row[5]}, Salary:{row[6]}, Bonus:{row[7]}, Total Salary:{row[8]}")

        cursor.close()
        connection.close()


# ---------------------------
# Update employee
# ---------------------------
def update_employee(emp_id, name, age, mobile, city, dept, salary, bonus, total_salary):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        sql = """UPDATE employee
                 SET emp_name=%s, emp_age=%s, mobile=%s, city=%s, department=%s,
                     salary=%s, bonus=%s, total_salary=%s
                 WHERE emp_id=%s"""

        values = (name, age, mobile, city, dept, salary, bonus, total_salary, emp_id)

        cursor.execute(sql, values)
        connection.commit()

        print("Employee updated successfully.")

        cursor.close()
        connection.close()


# ---------------------------
# Delete employee
# ---------------------------
def delete_employee(emp_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()

        sql = "DELETE FROM employee WHERE emp_id=%s"

        cursor.execute(sql, (emp_id,))
        connection.commit()

        print("Employee deleted successfully.")

        cursor.close()
        connection.close()


# ---------------------------
# Main menu
# ---------------------------
def main():

    while True:

        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Name: ")
            age = int(input("Age: "))
            mobile = input("Mobile: ")
            city = input("City: ")
            dept = input("Department: ")
            salary = int(input("Salary: "))
            bonus = int(input("Bonus: "))
            total_salary = salary + bonus

            add_employee(name, age, mobile, city, dept, salary, bonus, total_salary)

        elif choice == "2":
            view_employees()

        elif choice == "3":

            emp_id = int(input("Employee ID to update: "))

            name = input("Name: ")
            age = int(input("Age: "))
            mobile = input("Mobile: ")
            city = input("City: ")
            dept = input("Department: ")
            salary = int(input("Salary: "))
            bonus = int(input("Bonus: "))
            total_salary = salary + bonus

            update_employee(emp_id, name, age, mobile, city, dept, salary, bonus, total_salary)

        elif choice == "4":

            emp_id = int(input("Employee ID to delete: "))
            delete_employee(emp_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


# ---------------------------
# Run program
# ---------------------------
if __name__== "__main__":
    main()
