import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ashutosh',
    
)

# prepare a cursor object  
cursorObject = database.cursor()

# create a data base
cursorObject.execute("CREATE DATABASE elderco")

print('All Done!')