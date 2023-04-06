#to view the table
import sqlite3


conn = sqlite3.connect('Sage.db')

# retrieve data from the  table
cursor = conn.execute("SELECT * FROM ActivityLogs ORDER BY QueryNo DESC") 
for row in cursor:
    print(row)


conn.close()
