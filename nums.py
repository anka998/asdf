class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        return self.rate * self.days

worker = Worker("Иван", "Иванов", 1525, 20)
print(f"Зарплата работника: {worker.GetSalary()}")