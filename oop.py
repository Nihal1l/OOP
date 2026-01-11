class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Error: {self.__name} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Success: {self.__name} enrolled.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Error: {self.__name} is not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Success: {self.__name} dropped.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"ID: {self.__student_id} | Name: {self.__name} | Status: {status}")

Student(101, "Alice", "CS", True)
Student(102, "Bob", "Math", False)

while True:
    print("\n1. View All  2. Enroll  3. Drop  4. Exit")
    choice = input("Choice: ")

    if choice == "4": break
    
    if choice == "1":
        for s in StudentDatabase.student_list:
            s.view_student_info()

    elif choice in ["2", "3"]:
        search_id = int(input("Enter ID: "))
        found_student = None
        for s in StudentDatabase.student_list:

            if s.get_id() == search_id:
                found_student = s
        
        if found_student == None:
            print("Error: ID not found!")
        else:
            if choice == "2": found_student.enroll_student()
            else: found_student.drop_student()