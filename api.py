from fastapi import FastAPI
from pydantic import BaseModel
from tv import TV
from ac import AC
from speaker import Speaker
from remote import Remote

#uvicorn api:app --reload  here api is the filename api.py , app is variable we created and -reload = automatically restart the server when you change code (helpful while developing).

app = FastAPI()

class DeviceRequest(BaseModel):
    device: str

tv = TV("Living Room TV", "Sony")
ac = AC("Drawing Room", "Blue Star")
speaker = Speaker("Music Room", "Boat")

devices = {
    "tv": Remote(tv),
    "ac": Remote(ac),
    "speaker": Remote(speaker)
}

@app.get("/")
def read_root():
    return {"message" : "Universal remote api is running"}

@app.post("/power")
def power(request: DeviceRequest):
    remote = devices.get(request.device)
    if remote is None:
        return {"error": f"Unknown device: {request.device}"}
    remote.press_power()
    return {"Device" : remote.device.name, "is_on" : remote.device.is_on()}

@app.post("/volume_increase")
def volume_up(request: DeviceRequest):
    remote = devices.get(request.device)
    if remote is None:
        return {"error": f"Unknown device: {request.device}"}
    if not hasattr(remote.device, "get_volume"):
        return {"error": f"{remote.device.name} does not support volume control."}
    remote.press_volume_up()
    return {"Device": remote.device.name, "volume": remote.device.get_volume()}

@app.post("/volume_decrease")
def volume_down(request: DeviceRequest):
    remote = devices.get(request.device)
    if remote is None:
        return {"error": f"Unknown Device: {request.device}"}
    if not hasattr(remote.device, "get_volume"):
        return {"error": f"{remote.device.name} does not support volume control."}
    remote.press_volume_down()
    return {"Device": remote.device.name, "volume": remote.device.get_volume()}

@app.post("/mute")
def mute(request: DeviceRequest):
    remote = devices.get(request.device)
    if remote is None:
        return {"error": f"Unknown Device: {request.device}"}
    if not hasattr(remote.device, "is_muted"):
        return {"error": f"{remote.device.name} does not support mute."}
    remote.press_mute_toggle()
    return {"Device": remote.device.name, "muted": remote.device.is_muted()}