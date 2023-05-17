class Vehical:
    def __init__(self, color, capacity, engin_power, tyre):
        self.color = color
        self.capacity = capacity
        self.engin_power = engin_power
        self.tyre = tyre
        self.startCar = False

    def start(self):
        if self.startCar:
            return "car is already started"
        self.startCar = True
        return "car is started"

    def stop(self):
        if self.startCar:
            self.startCar = False
            return "car is stopped"

        return "car is already stopped"


class Car(Vehical):
    def __init__(self, color, capacity, engin_power, tyre, air_bags, gear, speed, fuel):
        super().__init__(color, capacity, engin_power, tyre)
        self.air_bags = air_bags
        self.gear = gear
        self.speed = speed
        self.fuel = fuel
        self.ac = False

    def accelerate(self):
        return "accelerate car"

    def fillFuel(self):
        return "filling fuel"

    def play_music(self):
        return "music is on"

    def onAC(self):
        if self.ac:
            return "ac is already on"
        self.ac = True
        return "ac is turend on"

tata = Car("blue", 5, 400, 4, 4, 5, 200, 20)
print(tata.start())
print(tata.stop())
print(tata.start())
print(tata.onAC())

class Electric_car(Vehical):
    def __init__(self, color, capacity, engin_power, tyre, battery):
        super().__init__(color, capacity, engin_power, tyre)
        self.battery = battery

    def charging(self):
            return "car is charging"

    def battery_level(self):
            if self.battery<=0:
                return "no charge"
            if self.battery<=4:
                return "warning! low charge"
            if self.battery<=9:
                return "ok charging level"
            if self.battery>=10:
                return "charge is full"

tata_eve = Electric_car("red", 5, 600, 4, 7)
print(tata_eve.charging())

print(tata_eve.battery_level())
