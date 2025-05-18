# Python program to manage student records using inheritance and error handling.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Marks:
    def __init__(self, grade):
        self.grade = grade

class Data(Person, Marks):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        Marks.__init__(self, grade)

    def display(self):  # Added 'self' to access instance attributes
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

try:
    n1 = input("Enter name: ")
    if not n1.isalpha():  # Only checks for valid name
        raise ValueError("Enter a valid name (only letters allowed).")

    n2 = int(input("Enter age: "))  # No error handling for age
    n3 = input("Enter grade: ")  # No error handling for grade

    output = Data(n1, n2, n3)
    output.display()  

except ValueError as e:
    print("Exception occurred:", e)

if __name__ == "__main__":
    record = Data("Asta", 20, "pass")
    record.display()
