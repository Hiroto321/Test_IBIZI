   import sqlite3

   def login(username, password):
       # УЯЗВИМОСТЬ: Захардкоженный пароль (Hardcoded password)
       if password == "SuperSecretPassword123!":
           conn = sqlite3.connect('users.db')
           cursor = conn.cursor()
           # УЯЗВИМОСТЬ: SQL Injection (строка собирается через конкатенацию)
           query = "SELECT * FROM users WHERE username = '" + username + "'"
           cursor.execute(query)
           return cursor.fetchone()
