class Airplane:
def **init**(self, model, manufacturer, capacity):
self.model = model
self.manufacturer = manufacturer
self.capacity = capacity

def take_off(self): # Add take-off logic here
pass

def land(self): # Add landing logic here
pass

def fly(self, destination): # Add flying logic here
pass

def **str**(self):
return f"Airplane: {self.model} - {self.manufacturer}"

def take_off(self):
print(f"The {self.model} is taking off.")

def land(self):
print(f"The {self.model} is landing.")

def fly(self, destination):
print(f"The {self.model} is flying to {destination}.")
print("Flying...")
print("Arrived at destination.")
print(f"The {self.model} has arrived at {destination}.")
