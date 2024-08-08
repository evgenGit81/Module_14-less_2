# -*- coding: utf-8 -*-
import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
    # """Вносим данные в базу"""
    # cursor.execute("INSERT INTO Users  (username, email, age, balance) VALUES(?, ?, ?, ?)",
    #                (f"User{i + 1}", f"example{i + 1}@gmail.com", f"{(i + 1)* 10}", f"{1000}"))
    # """Обновляем базу (обновляем баланс у каждой второй записи)"""
    # ind = (i + 1) % 2
    # if ind != 0:
    #     k = (i + 1)
    #     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", ('500', f"{k}"))
    # ind = 0
"""Удаляем каждую третью запись начиная с первой"""
# k = []
# for i in range(1, 11, 3):
#     k.append(i)
# for l in k:
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{l}",))

# """Выводим в консоль выборку записей где возраст не равен 60"""
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age <> ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

"""Удаление записи с id 6"""
# cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

"""Подсчет общего количества записей"""
cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]
print("Всего пользователей", total)

"""Рассчет суммы всех балансов"""
cursor.execute("SELECT SUM(balance) FROM Users")
sumres = cursor.fetchone()[0]
print("Суммарный баланс", sumres)

"""Рассчет среднего баланса"""
cursor.execute("SELECT AVG(balance) FROM Users")
middlebal = cursor.fetchone()[0]
print("Средний баланс", middlebal)

connection.commit()
connection.close()

