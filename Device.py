from abc import ABC, abstractmethod

class DeviceStateError(Exception):
    pass

class Device(ABC):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.__is_on = False

    def power_on(self):
        if self.__is_on:
            raise DeviceStateError(f"{self.name} is already on.")    
        self.__is_on = True
        print(f"{self.name} turned on successfully!")

    def power_off(self):
        if not self.__is_on:
            raise DeviceStateError(f"{self.name} is already off.")
        self.__is_on = False
        print(f"{self.name} turned off successfully.")

    @abstractmethod
    def increase(self):
        pass

    @abstractmethod
    def decrease(self):
        pass

    @classmethod
    def from_string(cls, data_string):
        name, brand = data_string.split(",")
        return cls(name, brand)  
    
class AudioDevice(Device):
    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.__is_muted = False

    def is_muted(self):
        self.__is_muted    

    def mute(self):
        if self.__is_muted:
            raise DeviceStateError("Already muted")
        self.__is_muted = True
        print("Muted")  

    def unmute(self):
        if not self.__is_muted:
            raise DeviceStateError("Already unmuted")
        self.__is_muted = False
        print("Unmuted")          

class TV(AudioDevice):
    def __init__(self, name, brand):
        super().__init__(name, brand) 
        self.__volume = 10
        self.__channel = 1   

    def increase(self):
        if self.is_muted():
            self.unmute()
            print("Unmuting...")
        if self.__volume == 100:
            print(f"Volume is at fullest.")
        else:
            self.__volume += 1
            print(f"Volume increased to {self.__volume}")

    def decrease(self):
        if self.is_muted():
            self.unmute()
            print("Unmuting...")
        if self.__volume == 0:
            print(f"Volume reaches at lowest.")
        else:
            self.__volume -= 1  
            print(f"Volume reduced to {self.__volume} ") 

    def channel_up(self):
        if self.__channel == 1000:
            print(f"you reach to last channel, there is no more channel left.")  
        else:
            self.__channel += 1
            print(f"Chanel increased to {self.__channel}")

    def channel_down(self):
        if self.__channel == 1:
            print(f"You cannot go below zero.")  
        else:
            self.__channel -= 1
            print(f"Channel reduced to {self.__channel}")

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

class Speaker(AudioDevice):
    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.__volume = 10
        self.__is_muted = False

    def increase(self):
        if self.is_muted() :
            self.unmute()
            print("Unmuting....")
        if self.__volume == 100:
            print(f"Volume is at fullest.")
        else:
            self.__volume += 1
            print(f"Volume increased to {self.__volume}")

    def decrease(self):
        if self.is_muted():
            self.unmute()
            print("Unmuting....")
        if self.__volume == 0:
            print(f"Volume reaches at lowest.")
        else:
            self.__volume -= 1  
            print(f"Volume reduced to {self.__volume} ")                                    
                            

tv = TV("Living Room TV", "Sony")
tv.power_on()
tv.increase()
tv.increase()
tv.decrease()
tv.power_off()     
tv.channel_down()
tv.channel_up()  

ac = AC("Hall", "Blue_Star")

ac.power_on()

try:
    ac.power_off()
except DeviceStateError as e:
    print(f"Error: {e}")    

items = [tv, ac]
for item in items:
    item.increase()   

ac = AC.from_string("Bedroom,Lg")
print(ac.name, ac.brand)
            

        
            
