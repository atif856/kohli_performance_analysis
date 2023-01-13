class Sensor():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__record_date = "2023-01-10"
        self.__version = "1.12.1"
        self.data = {}

    def get_record_date(self):
        print(f"The record date for {self.name} is {self.__record_date}")

    def get_version(self):
        print(f"The version for {self.name} is {self.__version}")

    def set_version(self, version):
        self.__version = version
        print("version updated seccessfully")
        # print(f"The version for {self.name} is {self.__version}")

    def add_data(self, time, data):
        self.data["data"] = data
        self.data["time"] = time
        print(
            f"Received {len(data)} points"
        )

    def clear_data(self):
        self.data = {}
        print("Data cleared")

sensor1 = Sensor(
    name = "sensor1",
    location = "kolkata"
)

print(sensor1.name)
print(sensor1.location)
# print(sensor1.__record_date)
# print(sensor1.__version)

sensor1.get_record_date()
sensor1.get_version()

sensor1.set_version("1.12.2")
sensor1.get_version()