#this code is used to create database and add values
#now this code is used to add the rows

import sqlite3
import datetime


conn = sqlite3.connect('sage.db')
#conn = sqlite3.connect('Sage.db')



#conn.execute('''CREATE TABLE ActivityLogs (
#                QueryNo INTEGER PRIMARY KEY AUTOINCREMENT,
#               Time TEXT NOT NULL,
#               Query TEXT NOT NULL);''')


def addlog(query):
    conn = sqlite3.connect('sage.db')
    timestamp = datetime.datetime.now()
    # insert data into the table
    conn.execute("INSERT INTO ActivityLogs (Time, Query) VALUES ( ?, ?)", (timestamp, query))
    conn.commit()

# commit changes and close connection
conn.commit()
conn.close()

