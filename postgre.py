import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="vae23_5h", host="127.0.0.1", port="5432")
cursor = conn.cursor()
conn.autocommit = True

# команда для создания базы данных metanit
sql = "CREATE DATABASE metanit"

# выполняем код sql
cursor.execute(sql)
print("База данных успешно создана")

cursor.close()  # закрываем курсор
conn.close()  # закрываем подключение
conn.close()


