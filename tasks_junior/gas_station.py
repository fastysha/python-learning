class Fuel:
    def __init__(self, name: str, price: int, capacity: int):
        self.name = name
        self.price = price
        self.capacity = capacity


class Station:
    def __init__(self, number, fuel: Fuel):
        self.number = number
        self.fuel = fuel


STATION_OUTPUT_FORMAT = "Available station number: {}. Price: {}"

station1 = Station(1, Fuel("95", 30, 100))
station2 = Station(2, Fuel("92", 27, 90))
station3 = Station(3, Fuel("GAS", 20, 120))

stations = [station1, station2, station3]

def find_desired_stations(stations: list[Station], rf, rc) -> list[Station]:
    filtered_stations = []
    for station in stations:
        if rf == station.fuel.name and rc <= station.fuel.capacity:
            filtered_stations.append(station)
    return filtered_stations

# def print_desired_stations(stations: list[Station], rf: str, rc: int):
#     for station in stations:
#         if rf == station.fuel.name and rc <= station.fuel.capacity:
#             print(STATION_OUTPUT_FORMAT.format(
#                 station.number, station.fuel.price))

total_capacity = 0
for station in stations:
    total_capacity += station.fuel.capacity    

while(total_capacity > 0):
    print('-----------------------------')
    print('Total cap: ', total_capacity)
    for station in stations:
        print(station.fuel.name, station.fuel.capacity)

    req = input("Please,enter fuel name and desired capacity: ")
    req_fuel = req.split(" ")[0]
    req_capacity = int(req.split(" ")[1])

    available_stations = find_desired_stations(stations, req_fuel,  req_capacity)

    if len(available_stations)==0:
        print(req_fuel,"is over, soryy!")
        continue

    for station in available_stations:
         print(STATION_OUTPUT_FORMAT.format(station.number, station.fuel.price))
    
    req_number = int(input("Enter station number: "))
    for station in stations:
        if req_number == station.number:
            station.fuel.capacity -= req_capacity
            print("You refueled for", req_capacity, "liters, the price is",
                  (station.fuel.price * req_capacity), "UAH")
            break

    total_capacity = 0
    for station in stations:
        total_capacity += station.fuel.capacity
else:
    print("Bye,bye")
