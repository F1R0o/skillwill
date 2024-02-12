
from abc import ABC,abstractmethod

class Vechile(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vechile):
    def __init__(self,max_speed,curent_speed):
        self.max_speed = max_speed
        self.curent_speed = curent_speed

    def start_engine(self):
        return "car started"
    
    def stop_engine(self):
        return 'car stopped'
    


class SportCar(Car):
    def stop_engine(self):
        self.curent_speed = 0
        print (f'sport {super().stop_engine()} and current speed = {self.curent_speed}')

    def start_engine(self):
        print (f'sport {super().start_engine()} and max_speed is {self.max_speed}')



c = SportCar(2,3)
c.start_engine()
print(c.curent_speed)
c.stop_engine()
print(c.curent_speed)
