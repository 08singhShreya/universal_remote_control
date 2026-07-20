class EngineTypeError(Exception):
    pass

class Engine:
    def __init__(self):
        self.__running = False

    def is_running(self):
        return self.__running
    
    def start_engine(self):
        if self.__running:
            raise EngineTypeError(f"Engine is already running.")
        self.__running = True
        print(f"Engine Starts.")

    def stop_engine(self):
        if not self.__running:
            raise EngineTypeError(f"Engine is currently on.")
        self.__running = False 
        print(f"Engine Stopped")   
        
class Car:
    def __init__(self, engine):
        self.engine = engine

    def toggle_engine(self):
        if self.engine.is_running():
            return self.engine.stop_engine()
        else:
            return self.engine.start_engine()
      

e = Engine()
car = Car(e)     
car.toggle_engine()
car.toggle_engine()
car.toggle_engine()    