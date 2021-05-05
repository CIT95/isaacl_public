#! python3

# Create a parent class and at least 2 child classes. Demonstrate my
# my understanding of inheritance.


# Parent class
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def introduction(self):
        print(f'Hello! My name is {self.name} and I am a {self.age} year old {self.gender}.')


# Child classes
class Occupation(Person):
    def __init__(self, name, gender, age, occupation):
        super().__init__(name, gender, age)
        self.occupation = occupation

    def introduction(self):
        print(f'Hello! My name is {self.name} and I am a {self.age} year old {self.gender}.')
        print(f'I also work as a {self.occupation}.')


class Student(Person):
    def __init__(self, name, gender, age, major):
        super().__init__(name, gender, age)
        self.major = major

    def introduction(self):
        print(f'Hello! My name is {self.name} and I am a {self.age} year old {self.gender}.')
        print(f'I am also studying {self.major}')


isaac = Person('Isaac', 'Male', 23)
isaac.introduction()

doctor = Occupation('John', 'male', 28, 'doctor')
doctor.introduction()

student = Student('Jill', 'female', 22, 'biology')
student.introduction()
