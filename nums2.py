import sqlite3

connection = sqlite3.connect('drinks.db')
cursor = connection.cursor()

def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            quantity INTEGER DEFAULT 0,
            price REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cocktails (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ingredient1 TEXT,
            ingredient2 TEXT,
            strength REAL,
            price REAL NOT NULL
        )
    ''')

    connection.commit()

def add_drink(name, drink_type, quantity, price):
    cursor.execute('''
        INSERT INTO drinks (name, type, quantity, price)
        VALUES (?, ?, ?, ?)
    ''', (name, drink_type, quantity, price))
    connection.commit()

def add_cocktail(name, ingredient1, ingredient2, strength, price):
    cursor.execute('''
        INSERT INTO cocktails (name, ingredient1, ingredient2, strength, price)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, ingredient1, ingredient2, strength, price))
    connection.commit()

def display_drinks():
    cursor.execute('SELECT * FROM drinks')
    drinks = cursor.fetchall()
    print("Напитки:")
    for drink in drinks:
        print(f"ID: {drink[0]}, Название: {drink[1]}, Тип: {drink[2]}, Количество: {drink[3]}, Цена: {drink[4]}")

def display_cocktails():
    cursor.execute('SELECT * FROM cocktails')
    cocktails = cursor.fetchall()
    print("Коктейли:")
    for cocktail in cocktails:
        print(f"ID: {cocktail[0]}, Название: {cocktail[1]}, Ингредиент 1: {cocktail[2]}, "
              f"Ингредиент 2: {cocktail[3]}, Крепость: {cocktail[4]}, Цена: {cocktail[5]}")

def sell_drink(drink_id, quantity):
    cursor.execute('SELECT quantity, price FROM drinks WHERE id = ?', (drink_id,))
    drink = cursor.fetchone()
    if drink and drink[0] >= quantity:
        new_quantity = drink[0] - quantity
        cursor.execute('UPDATE drinks SET quantity = ? WHERE id = ?', (new_quantity, drink_id))
        connection.commit()
        total_price = drink[1] * quantity
        print(f"Продано {quantity} единиц напитка ID {drink_id}. Общая цена: {total_price:.2f}")
    else:
        print("Недостаточно товара на складе или напиток не найден.")

def sell_cocktail(cocktail_id, quantity):
    cursor.execute('SELECT price FROM cocktails WHERE id = ?', (cocktail_id,))
    cocktail = cursor.fetchone()
    if cocktail:
        total_price = cocktail[0] * quantity
        print(f"Продано {quantity} единиц коктейля ID {cocktail_id}. Общая цена: {total_price:.2f}")
    else:
        print("Коктейль не найден.")

create_tables()

add_drink('Кока-Кола', 'безалкогольный', 156, 95)
add_drink('Водка', 'алкогольный', 50, 179)

add_cocktail('Мохито', 'Лимон', 'Мята', 8.0, 123)
add_cocktail('Куба Либре', 'Ром', 'Кока-Кола', 15.0, 300)

display_drinks()
display_cocktails()

sell_drink(1, 13)
sell_cocktail(1, 47)

sell_drink(2, 19)
sell_cocktail(2, 38)

connection.close()

