class Integer:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def display(self):
        print(f"Первое число: {self.a}, Второе число: {self.b}")

    def update(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def total(self):
        return self.a + self.b

    def max_value(self):
        return max(self.a, self.b)

nums = Integer(5, 21)
nums.display()
print("Сумма чисел:", nums.total())
print("Максимальное число:", nums.max_value())

nums.update(46, 8)
nums.display()
print("Сумма чисел:", nums.total())
print("Максимальное число:", nums.max_value())
