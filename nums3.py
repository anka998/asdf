class Calculation:
    def __init__(self):
        self.calculationLine = ""

    def SetCalculationLine(self, line):
        self.calculationLine = line
        print(f"Строка установлена: {self.calculationLine}")

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol
        print(f"Добавлен символ '{symbol}': {self.calculationLine}")

    def GetCalculationLine(self):
        print(f"Текущая строка: {self.calculationLine}")
        return self.calculationLine

    def GetLastSymbol(self):
        if self.calculationLine:
            print(f"Последний символ: {self.calculationLine[-1]}")
            return self.calculationLine[-1]
        print("Строка пустая, символ отсутствует")
        return None

    def DeleteLastSymbol(self):
        if self.calculationLine:
            removed = self.calculationLine[-1]
            self.calculationLine = self.calculationLine[:-1]
            print(f"Удалён последний символ '{removed}': {self.calculationLine}")
        else:
            print("Строка пустая, удалять нечего")

calc = Calculation()
calc.SetCalculationLine("123")
calc.SetLastSymbolCalculationLine("4")
calc.GetCalculationLine()
calc.GetLastSymbol()
calc.DeleteLastSymbol()
calc.GetCalculationLine()