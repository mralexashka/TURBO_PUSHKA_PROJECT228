import psycopg2

conn = psycopg2.connect(dbname="turbo_puska_db", user="postgres", password="alexashka", host="127.0.0.1", port="5432")
cursor = conn.cursor()
conn.autocommit = True


sql = "CREATE TABLE users (id SERIAL PRIMARY KEY, login VARCHAR(50),  password VARCHAR(30))"

# выполняем код sql
cursor.execute(sql)
print("База данных успешно создана")

cursor.close()  # закрываем курсор
conn.close()  # закрываем подключение


