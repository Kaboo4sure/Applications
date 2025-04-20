import yfinance as yf
import sqlite3

stocks = ['MTNN.LG', 'ZENITHBANK.LG', 'GTCO.LG', 'UBA.LG']

def fetch_and_store_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('naijastock.db')
    cursor = conn.cursor()

    for stock in stocks:
        # Fetch historical data from Yahoo Finance
        data = yf.download(stock, start='2022-01-01')

        for row in data.itertuples():
            # Insert data into the stock_data table
            cursor.execute('''
                INSERT INTO stock_data (date, ticker, open, high, low, close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (row.Index, stock, row.Open, row.High, row.Low, row.Close, row.Volume))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Data for {stock} inserted into database successfully.")

# Call the function to fetch and store data
fetch_and_store_data()
