import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('naijastock.db')
cursor = conn.cursor()

# Query the first few rows from the stock_data table
cursor.execute('SELECT * FROM stock_data LIMIT 10')

# Fetch and print the results
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the connection
conn.close()
