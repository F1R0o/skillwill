class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = {}
        self.average_qula = None

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        
    def average_point(self):
        only_grades = list(self.grades.values())
        if not only_grades:
            return 0
        self.average_qula = sum(only_grades) / len(only_grades)
        return self.average_qula

    def display_details(self):
        return f"{self.id},{self.name},{self.average_qula}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            return f"Student {name} with ID {student_id} added successfully."
        else:
            return f"Student with ID {student_id} already exists."
        
    def get_student_info(self, student_id):
        if student_id in self.students:
            return self.students[student_id].display_details()
        else:
            return f"Student with ID {student_id} does not exist."
    
        
    def show_student_average_grade(self, student_id):
        if student_id in self.students:
            return self.students[student_id].average_point()
        else:
            return f"Student with ID {student_id} does not exist."

student_system = StudentManagementSystem()
print(student_system.add_student("1", "John"))  
print(student_system.add_student("ID123", "Jane"))
print(student_system.get_student_info("1"))
print(student_system.show_student_average_grade("1"))
