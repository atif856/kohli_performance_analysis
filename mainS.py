from sensorModule import Sensor
from my_sensors import Accelerometer,Gyro,GPS
import numpy as np

# define a acclerometer object
acc = Accelerometer(
    name="Accelerometer_v1",
    location="Haldia",
    record_date="2023-01-10"
)

gyro = Gyro(
    name="Gyroscope_v1",
    location="Kolkata",
    record_date="2023-01-10"
)

gps = GPS(
    name="GPS_v1",
    location="Kolkata",
    record_date="2023-01-10",
    brand="Express1"
)

# get data
time = np.arange(10)
acc_data = np.random.randint(-20, 20, 10)
gyro_data = np.random.randint(-10, 30, 10)
gps_data = np.random.randint(-10, 5, 10)

# add data to sensors
acc.add_data(data=acc_data, time=time)
gyro.add_data(time, gyro_data)
gps.add_data(time, gps_data)

# print data points
print("Accelerometer data: \n",acc.data)
print("Gyroscope data: \n",gyro.data)
print("GPS data: \n",gps.data)