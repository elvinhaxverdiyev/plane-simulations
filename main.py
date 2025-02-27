class Plane:
    def __init__(self, name, capacity, speed):
        self.name = name
        self.capacity = capacity  
        self.speed = speed
        self.passengers = []
        self.is_flying = False  
        
    def load_speed(self, amount):
        new_speed = self.speed + amount
        self.speed = min(new_speed, 900)  
        return f"Speed load to {self.speed} km/h"
        
    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            return f"Passenger {name} added. Total passengers: {len(self.passengers)}"
        return "Capacity is full"
        
    def take_off(self):
        if self.passengers and self.speed > 0:
            self.is_flying = True
            return "The plane was take off."
        return "The Plane is empty"
        
    def land(self):
        self.is_flying = False
        self.speed = 0
        return "The plane was landed."
        
    def remove_passenger(self, name):
        if not self.is_flying and self.speed == 0:
            if name in self.passengers:
                self.passengers.remove(name)
                return f"Passenger {name} removed. Remaining passengers: {len(self.passengers)}"
            return "Passenger not found"
        return "Plane is flying, cannot remove passenger."
        
    def status(self):
        status = "flying" if self.is_flying else "not flying"
        return f"Plane: {self.name}\nSpeed: {self.speed} km/s\nPassengers: {len(self.passengers)}\nStatus: {status}"


plane1 = Plane("Boeing", 200, 0)

print(plane1.add_passenger("Elvin"))
print(plane1.load_speed(500))
print(plane1.take_off())
print(plane1.land())
print(plane1.remove_passenger("Elvin"))
print(plane1.status())