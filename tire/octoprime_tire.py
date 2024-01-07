from tire.tire import Tire

class Octoprime(Tire):
    def __init__(self, tire_weariness):
         self.tire_weariness = tire_weariness
    
    def needs_service(self):
        sum = 0
        for i in self.tire_weariness:
            sum = sum + i
        
        if sum >= 3.0:
            return True