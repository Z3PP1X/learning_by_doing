class Counter:
    def __init__(self, startwert, min_value=0, max_value=None):
        if max_value is None:
            max_value = startwert
        if startwert != min_value:
            startwert = min_value
        
        self.min_value = min_value
        self.max_value = max_value
        self.set_counter(startwert)

    def set_counter(self, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Der Wert {value} ist außerhalb der zulässigen Grenzen (min_value: {self.min_value}, max_value: {self.max_value}).")
        self.counter = value

    def weiter(self):
        if self.counter < self.max_value:
            self.counter += 1
        else:
            print("Counter hat den maximalen Wert erreicht!")

    def zurueck(self):
        if self.counter > self.min_value:
            self.counter -= 1
        else:
            print("Counter hat den minimalen Wert erreicht!")

    def wert(self):
        return self.counter
    
test = Counter(startwert=0, min_value=10, max_value=50)
print(test.counter)