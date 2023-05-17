import datetime

class Watch:
        def __init__(self, type):
            time = datetime.datetime.now()
            self.hr = time.hour
            self.min = time.minute
            self.sec = time.second
            self.alarm = None
            self.type = type

        def showTime(self):
            return f"current tiem is - {self.hr}:{self.min}:{self.sec}"

        def set_alarm(self, hr, min, sec=00):
            self.alarm = f"{hr}:{min}:{sec}"
            return f"alarm set for {self.alarm}"

        def stop_alarm(self):
            self.alarm = None
            return "alram is turend off"

time = Watch("analog")
print(time.set_alarm(3,15,00))
print(time.showTime())
print(time.stop_alarm())



