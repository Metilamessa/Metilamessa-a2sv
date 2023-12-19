class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # {id: (station, t)}
        self.travel_times = {}  # {(startStation, endStation): (total_time, count)}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins[id]
        end_station = stationName
        travel_key = (start_station, end_station)

        total_time, count = self.travel_times.get(travel_key, (0, 0))
        total_time += t - check_in_time
        count += 1

        self.travel_times[travel_key] = (total_time, count)
        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_key = (startStation, endStation)
        total_time, count = self.travel_times[travel_key]
        return total_time / count if count > 0 else 0



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)