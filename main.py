from tv import TV
from ac import AC
from speaker import Speaker
from remote import Remote


tv = TV("Living Room TV", "Sony")
ac = AC("Hall", "Blue Star")
speaker = Speaker("Music Room", "Boat")

remotes = [Remote(tv), Remote(ac), Remote(speaker)]

for remote in remotes:
    remote.press_power()
    remote.press_volume_down()
    remote.press_volume_down()
    remote.press_volume_up()
    remote.press_volume_up()
    remote.press_volume_up()
    remote.press_volume_up()
    remote.press_mute_toggle()
    remote.press_mute_toggle()
    remote.press_mute_toggle()
    remote.press_power()
    remote.press_power()


remote._log("Test_action", "success")

            