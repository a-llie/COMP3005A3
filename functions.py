import psycopg2

optionsList = """\n   1:  Get All Students 
   2:  Insert a New Student
   3:  Update a Student's Email
   4:  Delete a Student
Else:  Quit\n"""

# getAllStudents()
# Retrieves and displays all records from the students table.
def getAllStudents():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students")
        print(cur.fetchall())


# addStudent(first_name, last_name, email, enrollment_date)
# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        conn.commit()

# updateStudentEmail(student_id, new_email)
# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    with conn.cursor() as cur:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        conn.commit()   


# deleteStudent(student_id)
# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id))
        conn.commit()   


# getNewStudentDetails()
# Prompts the user to enter the details of a new student.
def getNewStudentDetails():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    email = input("Enter the student's email: ")
    enrollment_date = input("Enter the student's enrollment date: ")
    return first_name, last_name, email, enrollment_date


# getUpdateStudentDetails()
# Prompts the user to enter the student_id and the new email address for the student.
def getUpdateStudentDetails():
    student_id = getStudentId()
    new_email = input("Enter the student's new email: ")
    return student_id, new_email

# getStudentId()
# Prompts the user to enter the student_id of the student.
def getStudentId():
    student_id = input("Enter the student's ID: ")
    return student_id

# prompt()
# Prompts the user to choose an option from the optionsList.
def prompt():
    i = input(f' \n{optionsList} \n>> ')
    match i:
        case "1":
            getAllStudents()
        case "2":
            first_name, last_name, email, enrollment_date = getNewStudentDetails()
            addStudent(first_name, last_name, email, enrollment_date)
        case "3":
            student_id, new_email = getUpdateStudentDetails()
            updateStudentEmail(student_id, new_email)
        case "4":
            student_id = getStudentId()
            deleteStudent(student_id)
        case _:
            exit()


if __name__ == "__main__":
    db = input("Enter database name\n>>")
    user =  input("Enter username\n>>")
    pw = input("Enter password\n>>")

    with psycopg2.connect(f'dbname={db} user={user} password={pw}') as conn:
        print('Choose one of the following options: ')
        while True:
            prompt()



