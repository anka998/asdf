import psutil

import sqlite3
from datetime import datetime

connection = sqlite3.connect('system_monitor.db')
cursor = connection.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS monitoring (
            id INTEGER PRIMARY KEY,
            timestamp TEXT NOT NULL,
            cpu_usage REAL NOT NULL,
            memory_usage REAL NOT NULL,
            disk_usage REAL NOT NULL
        )
    ''')
    connection.commit()

def record_monitoring():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
        INSERT INTO monitoring (timestamp, cpu_usage, memory_usage, disk_usage)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, cpu_usage, memory_usage, disk_usage))

    connection.commit()

def view_monitoring_data():
    cursor.execute('SELECT * FROM monitoring')
    records = cursor.fetchall()

    for record in records:
        print(f"ID: {record[0]}, Time: {record[1]}, CPU: {record[2]}%, Memory: {record[3]}%, Disk: {record[4]}%")

create_table()

for _ in range(5):
    record_monitoring()

view_monitoring_data()

connection.close()


