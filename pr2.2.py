class Train:
    def __init__(self, destination, train_num, departure_time):
        self.destination = destination
        self.train_num = train_num
        self.departure_time = departure_time

    def print_info(self):
        print(f"Поезд номер: {self.train_num}\nПункт назначения: {self.destination}"
              f"\nВремя отправления: {self.departure_time}")

trains = [
    Train("Москва", "154", "09:00"),
    Train("Казань", "232", "10:30"),
    Train("Сочи", "163", "15:45")
]
search_num = input("Введите номер поезда для поиска: ")
for train in trains:
    if train.train_num == search_num:
        train.print_info()
        break
else:
    print("Поезд не найден.")
