import psycopg2

conn = psycopg2.connect(dbname="turbo_puska_db", user="postgres", password="alexashka", host="127.0.0.1", port="5432")
cursor = conn.cursor()
conn.autocommit = True


sql = "CREATE TABLE notes (id INTEGER, note TEXT)"

# выполняем код sql
cursor.execute(sql)
print("Таблица данных успешно создана")

cursor.close()  # закрываем курсор

conn.close()  # закрываем подключение


