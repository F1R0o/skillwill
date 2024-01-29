

# class Car:

#     wheel_amount = 4

#     def __init__(self,color):
#         self._color = color

#     @property
#     def color(self):
#         return self._color

#     @color.setter
#     def color(self, color):
#         if not isinstance(color,str):
#             print("wrong vallue")
#         else:
#             self._color = color

# c = Car("witeli")
# c.color  = 23
# print(c.color)


class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = False

    @property
    def get_brand(self):
        return (f"maqnaqnis brendi aris:{self.__brand}")

    
    @property
    def get_model(self):
        return (f"maqnaqnis modeli aris:{self.__model}")
        
    
    @property
    def get_production_year(self):
        return (f"maqnaqnis gamoshvebis weli aris:{self.__production_year}")
    
    @property
    def get_color(self):
        return (f"maqnaqnis  feri aris:{self.__color}")
        
    
    @property
    def get_horse_power(self):
        return (f"maqnaqnis cxenis dzala aris:{self.__horse_power}")


    # @property
    # def get_sport_car(self):
    #     return self.__is_sport_car
    
    @get_color.setter
    def change_colour(self, new_colour):
        if  isinstance(new_colour,str):

            if new_colour == self.__color :
                print("feri igivea")
            else:
                print("feri sheicvala ")
                self.__color = new_colour
        else:
            print("shen unda sheiyvaneo stringi ")

    @get_horse_power.setter
    def increase_horse_power(self,hp):
        if isinstance (hp,int):
            if hp > 0:
                print("cxenis dzala warmatebit sheicaval ")
                self.__horse_power += hp
            elif hp <= 0 :
                print("0ze nakelbs rogor umateb? ")
        else:
            print("shen unda sheiyvano intigeri ")
    

car = Car('mersedes', "mersedes1", 2, "witeli", 222, False)

print(car.get_horse_power)
car.increase_horse_power = 2
print(car.get_horse_power)
car.increase_horse_power = 100
print(car.get_horse_power)
car.__is_sport_car = True
print(car.__is_sport_car)

