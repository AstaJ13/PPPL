class Person: 
    def __init__(self, name, age): 
        if not name or type(name) != str: 
            raise ValueError("Name must be a non-empty string.") 
        if type(age) != int or age < 0: 
            raise ValueError("Age must be a non-negative integer.") 
        self.name = name 
        self.age = age 

    def __str__(self): 
        return "Name: " + self.name + ", Age: " + str(self.age) 
 
class Student(Person): 
    def __init__(self, name, age, student_id): 
        super().__init__(name, age) 
        if not student_id or type(student_id) != str: 
            raise ValueError("Student ID must be a non-empty string.") 
        self.student_id = student_id 
        self.grades = {} 

    def add_grade(self, subject, grade): 
        if not subject or type(subject) != str: 
            raise ValueError("Subject must be a non-empty string.") 
        if type(grade) not in [int, float] or not (0 <= grade <= 100): 
            raise ValueError("Grade must be a number between 0 and 100.") 
        self.grades[subject] = grade 

    def get_average_grade(self): 
        if not self.grades: 
            return 0 
        return sum(self.grades.values()) / len(self.grades) 

    def __str__(self): 
        grades_str = ", ".join(subject + ": " + str(grade) for subject, grade in self.grades.items()) 
        return super().__str__() + ", Student ID: " + self.student_id + ", Grades: {" + grades_str + "}" 

# Testing the class
try: 
    student = Student("ASTA",20,"0231") 
    student.add_grade("Python", 80) 
    student.add_grade("OS", 80) 
    print(student) 
    print("Average Grade: {:.2f}".format(student.get_average_grade())) 
except ValueError as e: 
    print("Error: " + str(e))
