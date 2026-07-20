from device import AudioDevice

class Speaker(AudioDevice):
    def __init__(self, name, brand):
        super().__init__(name, brand)
        self.__volume = 10

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
