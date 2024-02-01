


class Student:

    univerity = "KIU"

    def __init__(self,name,grade,age):
        self.__name = name
        self.__grade = grade
        self.__age = age


    def __str__(self):
        return (f"studenitis saxeli:{self.__name}\nasaaki:{self.__age}\nnishani:{self.__grade}")
    
    @property
    def is_passing(self):
        if self.__grade > 60:
            return True
        else:
            return False
        
    def increase_grade(self,grade):
        if isinstance(grade,int):
            self.__grade += grade
        else:
            return False
            
      

s = Student("luka",20,23)
s.increase_grade(100)
print(s.is_passing)