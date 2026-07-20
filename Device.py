from abc import ABC, abstractmethod

class DeviceStateError(Exception):
    pass

class Device(ABC):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.__is_on = False

    def is_on(self):
        return self.__is_on    
    
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
        return self.__is_muted    

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

      
