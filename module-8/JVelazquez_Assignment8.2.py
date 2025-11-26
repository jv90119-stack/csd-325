import json

def load_students(filename):
    with open(filename, 'r') as file:
        students = json.load(file)
    return students

def print_students(student_list):
    for student in student_list:
        print(student)

def main():
    filename = "student.json" 

    students = load_students(filename)

    print("\n Original Student List ")
    print_students(students)

    # New student data
    new_student = {
        "F_Name": "Jose",
        "L_Name": "Velazquez",
        "Student_Id": "50995",
        "Email": "jvelazquez@gmail.com"
    }

    students.append(new_student)

  
    print("\n Updated Student List ")
    print_students(students)

    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)

    print("\nThe JSON file has been successfully updated.")

main() 