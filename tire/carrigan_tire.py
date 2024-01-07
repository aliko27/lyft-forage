from tire.tire import Tire

class Carrigan(Tire):
    def __init__(self, tire_weariness):
        self.tire_weariness = tire_weariness
    
    def needs_service(self):
        for i in self.tire_weariness:
            if i >= 0.9:
                return True