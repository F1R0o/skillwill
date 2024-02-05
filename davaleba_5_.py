
class PersonMixin:
    def display_attributes(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Person,PersonMixin):
    def __init__(self, university, name, surname):
        self.university = university
        super().__init__(name, surname)








student1 = Student("sadme","luka","firuashvili")
student1.display_attributes()
