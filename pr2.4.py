class SimpleCounter:
    def __init__(self, initial=0):
        self.count = initial

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    @property
    def current_count(self):
        return self.count

counter = SimpleCounter(5)
print("Начальное значение счетчика:", counter.current_count)

counter.increment()
print("После увеличения:", counter.current_count)

counter.decrement()
print("После уменьшения:", counter.current_count)

