class FrequencyTracker:
    def __init__(self):
        self.count = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        self.count[self.frequency[number]] -= 1
        self.frequency[number] += 1
        self.count[self.frequency[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.frequency[number] == 0:
            return
        self.count[self.frequency[number]] -= 1
        self.frequency[number] -= 1
        self.count[self.frequency[number]] += 1

    def hasFrequency(self, freq: int) -> bool:
        return self.count[freq] > 0