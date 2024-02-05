
class PersonMixin:
    def display_attributes(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


class Person:
    def __init__(self, name, surname,age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person,PersonMixin):
    def __init__(self, university, name, surname,age):
        self.university = university
        super().__init__(name, surname,age)








student1 = Student("sadme","luka","firuashvili",20)
student1.display_attributes()
