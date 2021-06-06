import psycopg2

conn = psycopg2.connect(
    database = 'kivano',
    user = 'aimira', 
    password = '123456789',
    host = 'localhost',
    port = 5432
)

cur = conn.cursor()

# cur.execute('CREATE TABLE users (id SERIAL PRIMARY KEY, login VARCHAR(50), password VARCHAR(50))')
# conn.commit()
# cur.execute("INSERT INTO users(login, password) VALUES ('koko', '12345')")
# conn.commit()

cur.execute('SELECT * FROM users')
print (cur.fetchall())