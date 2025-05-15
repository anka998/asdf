class Features:
    def __init__(self, attr1=0, attr2=0):
        self.attr1 = attr1
        self.attr2 = attr2

    def attributes(self):
        print(f"Свойство 1: {self.attr1}, Свойство 2: {self.attr2}")

    def __del__(self):
        print(f"Объект удален с атрибутами: {self.attr1}, {self.attr2}")

obj = Features(50, 324)
obj.attributes()
del obj
