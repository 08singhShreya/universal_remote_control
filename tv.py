from device import Device, AudioDevice

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



