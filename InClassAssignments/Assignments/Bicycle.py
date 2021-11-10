class Bicycle:
    gear = 0
    speed = 0
    def __init__(self, g, s):
        self.gear = g
        self.speed = s

    def brake(self, decrement):
        self.speed-=decrement
    
    def speedup(self,increment):
        self.speed+=increment

    def status(self):
        print("Your speed is: ", self.speed, " and you gear is: ", self.gear)
    
class mountainBike(Bicycle):
    seatHeight = 0
    def __init__(self, g, s, sh):
        super().__init__(g, s)
        self.seatHeight = sh

    def status(self):
        print("Your speed is: ", self.speed, " and you gear is: ", self.gear, " and your seat height is: ", self.seatHeight)

mountainbike1= mountainBike(9,18,2)
bike = Bicycle(4,23)
print("the status before change in speed")
print("mountain bike status is: ")
mountainbike1.status()
print("Bicycle Bike status it: ")
bike.status()

mountainbike1.speedup(9)
bike.brake(2)

print("the status after change in speed")
print("mountain bike status is: ")
mountainbike1.status()
print("Bicycle status is: ")
bike.status()