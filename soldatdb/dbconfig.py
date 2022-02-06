import sqlite3

conn = sqlite3.connect('soldatdata.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
c.execute('''CREATE TABLE VALUE
             (sold INTEGER)''')
                 
conn.commit()

