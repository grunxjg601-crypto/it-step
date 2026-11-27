
import sqlite3

conn = sqlite3.connect("FruitBasket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Color TEXT
)
""")

cursor.execute("DELETE FROM Fruits")

fruits = [
    ("Яблуко", "Червоне"),
    ("Банан", "Жовтий"),
    ("Апельсин", "Помаранчевий")
]

cursor.executemany(
    "INSERT INTO Fruits (Name, Color) VALUES (?, ?)", fruits
)

cursor.execute("""
UPDATE Fruits
SET Color = 'Зелене'
WHERE Name = 'Яблуко'
""")

print("Фрукти жовтого кольору:")
cursor.execute("SELECT * FROM Fruits WHERE Color = 'Жовтий'")
print(cursor.fetchall())

print("\nВсі фрукти:")
cursor.execute("SELECT * FROM Fruits")
print(cursor.fetchall())

conn.commit()
conn.close()
