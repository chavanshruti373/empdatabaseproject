import mysql.connector

def connectDB():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="office"

    )
    
def insert_employee():
    name=input("Enter Employee name: ")
    dept=input("Enter Department: ")
    salary=int(input("Enter salary: "))

    conn=connectDB()
    cur=conn.cursor()
    cur.execute("Insert into employees(name, department, salary) values (%s,%s,%s)",
                (name,dept,salary))
    
    conn.commit()
    conn.close()
    print("Employee added successfully")

def view_employees():
    conn=connectDB()
    cur=conn.cursor()

    cur.execute("Select * from employees")

    for row in cur.fetchall():
        print(row)

    conn.close()
def menu():
    while True:
        print("-----------Employee Management--------------")
        print("1.Add Employee")
        print("2.view Employee")
        print("3.Exit")
        choice=int(input("Enter choice: "))

        if choice==1:
            insert_employee()

        elif choice==2:
            view_employees()
        else:
            print("Invalid choice! try again\n")

menu()

