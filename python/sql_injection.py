
import sqlite3, sys
conn = sqlite3.connect('test.db')
user_id = sys.argv[1]
# VULNERABLE: string formatting in SQL
query = f"SELECT * FROM users WHERE id = {user_id}"  # CWE-89
print(conn.execute(query).fetchall())
