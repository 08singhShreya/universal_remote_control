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

class CreateDeviceRequest(BaseModel):
    device_type: str
    name: str
    brand: str

devices = {
    "tv": Remote(tv),
    "ac": Remote(ac),
    "speaker": Remote(speaker)
}

@app.get("/")
def read_root():
    return {"message" : "Universal remote api is running"}

@app.post("/devices")
def create_device(request: CreateDeviceRequest):
    if request.device_type == "tv":
        new_device = TV(request.name, request.brand)
    elif request.device_type == "ac":
        new_device = AC(request.name, request.brand)
    elif request.device_type == "speaker":
        new_device = Speaker(request.name, request.brand)
    else:
        return {"error": f"Unknown Device Type: {request.device_type}"}

    remote = Remote(new_device)
    devices[new_device.name] = remote
    return {"message": f"{new_device.name} created successfully", "device_id": new_device.name}

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