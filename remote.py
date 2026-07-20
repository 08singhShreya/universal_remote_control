from device import Device, DeviceStateError
from datetime import datetime

class Remote:
    def __init__(self, device):
        self.device = device

    def _log(self, action, status):   
        timestamp = datetime.now()

        with open("remote_log.txt", "a") as f:
            f.write(f"{self.device.name} | {action} | {status} | {timestamp}\n ") 

    def press_power(self):
        try:
            if self.device.is_on():
                self.device.power_off()
            else:
                self.device.power_on()
            self._log("Power", "success")
        except DeviceStateError as e:
            self._log("Power", "failed")
            print(f"Error: {e}")    
        
    def press_volume_up(self):
        try:
            self.device.increase() 
            self._log("Volume", "success")
        except DeviceStateError as e:
            self._log("Volume", "failed")
            print(f"Error: {e}")     

    def press_volume_down(self):
        try:
            self.device.decrease()
            self._log("Volume", "success")
        except DeviceStateError as e:
            self._log("Volume", "failed")
            print(f"Error: {e}")   

    def press_mute_toggle(self):
        if not hasattr(self.device, "mute"):
            print(f"{self.device.name} does not support mute.")
            return
        try:
            if self.device.is_muted():
                self.device.unmute()
            else:
                self.device.mute()
            self._log("Mute", "success")
        except DeviceStateError as e:
            self._log("Mute", "failed")
            print(f"Error: {e}")       