from datetime import datetime as dt

# This is Adaptee class
class Test:
    def __init__(self, date, time, speed, distance, desc) -> None:
        self.date = date
        self.time = time
        self.speed = speed
        self.distance = distance
        self.desc = desc

    def get_data(self):
        return self.__dict__

# Structural Pattern: Adapter is used here
# uses Adaptee (Test) class method get_data(), and 
# makes data compatible with 'New' application
class TestAdapter(Test):
    def __init__(self, date, time, speed, distance, desc) -> None:
        super().__init__(date, time, speed, distance, desc)

    def get_data_new(self) -> None:
        data = self.get_data()
        if 'PM' in data['time']:
            time = str(int(data['time'][:1])+12)+data['time'][1:-3]
        elif 'AM' in data['time']:
            time = data['time'][:-3]
        return {
            'date' : dt.strptime(data['date'], "%Y/%d/%m").strftime("%d.%m.%Y"),
            'time' : time,
            # 'time' : dt.strptime(data['time'], "%I:%M:%S %p").strftime("%H:%M:%S"),
            # For some reason ^-function returns (ValueError: unconverted data remains: AM/PM) 
            'speed' : str(round(float(data['speed']) * 1.943844, 2)),
            'distance' : str(round(float(data['distance'].replace(',', '.')) * 0.5399565, 2)),
            'desc' : data['desc']
        }

# For testing purposes, while runung as standalone module
if __name__ == '__main__':
    data = [{'date': '2021/01/09',
        'time': '1:00:10 PM',
        'speed': '10',
        'distance': '3,0',
        'desc': 'First test'}]
    test = Test(**data[0])
    print(test.get_data(),"\n")

    print("="*40)
    test_adapted = TestAdapter(**data[0])
    print(test_adapted.get_data())
    print(test_adapted.get_data_new())
    
