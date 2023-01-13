class Sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self, time, data):
        self.data["data"] = data
        self.data["time"] = time
        print(
            f"Received {len(data)} points"
        )

    def clear_data(self):
        self.data = {}
        print("Data cleared")

import numpy as np

sensor1 = Sensor(
    name="sensor1",
    location="Haldia",
    record_date="2023-01-09"
)

print(sensor1.name, sensor1.location, sensor1.record_date)

# generating random data of length 10
data = np.random.randint(-10, 10, 10)    #randint(lower range, upper range, length of data)

# generating random time in seconds corresponding to the data points above
time = np.arange(10)     #arange(time in seconds)
# print(data)
# print(time)


# adding the generated data points into the sensor object
sensor1.add_data(
    time=time,
    data=data
)

# printing the sensor dictionary within the class
print(sensor1.data)    # data --> empty dictionary

print("------------------------")

class Accelerometer(Sensor):
    def show_type(self):
        print(f"I am an {self.name}")

acc = Accelerometer(
    "accelerometer",
    "Haldia",
    "2020-01-09"
)

acc.show_type()

data = np.random.randint(-10, 10, 10)
time = np.arange(10)
acc.add_data(
    data=data,
    time=time   #OR np.arange(10)
)
print(acc.data)

print("---------------------------")

class Gyro(Accelerometer):
    def show_type(self):
        print(f"\nThis is {self.name} and location is at {self.location}")


accl = Accelerometer(
    "accelerometer",
    "Haldia",
    "2020-01-09"
)

accl.show_type()

data = np.random.randint(-10, 10, 10)
time = np.arange(10)
accl.add_data(
    data=data,
    time=time   #OR np.arange(10)
)
print("Accelerometer data: ", accl.data)

gyro  = Gyro(
    name="Gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
)

gyro_data = np.random.randint(-25, 5, 10)
gyro_time = np.arange(10)

gyro.add_data(
    data=gyro_data,
    time=gyro_time
)
gyro.show_type()
# print("Gyroscope data: ", gyro.data)


print("-------------------------------")
class GPS(Sensor):
    def __init__(self,name,location,record_date,brand):
        super().__init__(                            # taking parameter from super class
            name,location,record_date
        )
        self.brand = brand



gps = GPS(
    name="GPS",
    location="Delhi",
    record_date="2023-01-10",
    brand="express1"
)

print(gps.name, gps.location, gps.record_date)
print(gps.brand)