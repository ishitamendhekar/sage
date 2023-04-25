#DESC ActivityLogs
import sqlite3

# connect to the database
conn = sqlite3.connect('Sage.db')

# get the column information for the table
result_set = conn.execute('PRAGMA table_info(ActivityLogs)')

# display the column information
print('Column Name  Data Type     Allow NULL  Primary Key  Autoincrement')
print('---------------------------------------------------------------')
for row in result_set:
    print('{:<12}  {:<12}  {:<10}  {:<11}  {}'.format(row[1], row[2], 'YES' if row[3] else 'NO', 'YES' if row[5] else 'NO', 'YES' if row[5] else 'NO'))

# close the connection
conn.close()
