
class Heart:
    def __init__(self):
        self.__state = ''

    
    def check_activity(self, load_percentage):
        if isinstance(load_percentage,int) or isinstance(load_percentage,float):
            if load_percentage >= 70:
                self.__state = "hihgh blood presure"
            else:
                self.__state = 'feeling good'
        else:
            print("shen unda sheiyvano  float an int")
        return self.__state


class Brain:
    def __init__(self):
        self.__state = ''
    
    def check_activity(self,tired_precentage):
        if isinstance(tired_precentage,int) or isinstance(tired_precentage,float):
            if tired_precentage  >= 90:
                self.__state  = 'tired'
            else:
                self.__state = 'reset'
        else:
            print("shen unda sheiyvano float an int")
        return self.__state




class Leg:
    def __init__(self, person_instance, moving_speed):
        self.__moving_speed = moving_speed
        self.__person = person_instance

    @property
    def moving_speed(self):
        return self.__moving_speed

    def determine_speed_status(self):
        if self.__moving_speed > 10:
            return "running"
        elif 0 < self.__moving_speed <= 10:
            return "walking"
        else:
            return "standing"
        
class Person:
    def __init__(self):
        self.usage = {
            "brain":Brain(),
            "heart":Heart()
        }




p = Person()
print(p.usage.get("brain").check_activity(30))
print(p.usage.get("heart").check_activity(50))
z = Leg(p, 20)  


print("Leg speed:", z.moving_speed)
print("Speed status:", z.determine_speed_status())



