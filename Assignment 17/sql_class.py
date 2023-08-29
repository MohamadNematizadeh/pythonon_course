import sqlite3

data = sqlite3.connect("data_test.db")

c = data.cursor()

try:
    c.execute("""
    CREATE TABLE customers (
        firstname TEXT,
        lastname TEXT,
        email TEXT
    )
""")
except:
    pass

# c.execute("INSERT INTO customers VALUES ('kiya', 'keynia', 'kiyakeynia@gmail.com')")

# many_customers = [('kiya', 'keynia', 'kiyakeynia@gmail.com'), ('amir', 'jahan bakhsh', 'amirreza jahan bakhsh@gmail.com')]
# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

c.execute("SELECT * FROM customers")

# itames = c.fetchall()
# print(itames)

# itame = c.fetchone()
# print(itame)

u_itame = c.fetchmany(2)
# print(u_itame)

# c.execute("SELECT * FROM customers")
# c.execute("SELECT email FROM customers")
c.execute("SELECT * FROM customers WHERE firstname LIKE 'a%'")

itames = c.fetchall()

for i in itames:
    print(i)

c.execute("UPDATE customers SET firstname = 'ahmad' WHERE firstname = 'kiya'")

c.execute("DELETE FROM customers WHERE firstname = 'mamad'")

c.execute("SELECT * FROM customers")

itames = c.fetchall()
for i in itames:
    print(i)

# c.execute("SELECT * FROM customers ORDER BY firstname")
c.execute("SELECT * FROM customers ORDER BY firstname DESC")

itames = c.fetchall()
for i in itames:
    print(i)

# c.execute("DROP TABLE customers")

# c.execute("SELECT * FROM customers")

itames = c.fetchall()
for i in itames:
    print(i)

data.commit()

data.close()