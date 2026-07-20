from device import Device

class AC(Device):
    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.__temperature = 24

    def increase(self):
        if self.__temperature == 30:
            print(f"you are already at ceiling point- {self.__temperature}, can't go higher.")  
        else:
            self.__temperature += 1   
            print(f"Temperature increased to {self.__temperature}")

    def decrease(self):
        if self.__temperature == 16:
            print(f"You already hit ground point - {self.__temperature}, can't go down.")
        else:
            self.__temperature -= 1
            print(f"Temperature decreased to {self.__temperature}")   