import sqlite3

conn = sqlite3.connect("PersonalAi.db")

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null,'android studio', 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null,'mahadbt', 'https://mahadbt.maharashtra.gov.in/Login/Login')"
# cursor.execute(query)
# conn.commit()

query = "UPDATE web_command SET name = 'maha dbt' WHERE id=4;"
cursor.execute(query)
conn.commit()