# from alpha_vantage.timeseries import TimeSeries
# API_Key = 'J63G1AJ3FL74N43G'
# ts = TimeSeries(key = API_Key, output_format = 'pandas')
# data = ts.get_monthly_adjusted('AAPL')
# print(data[0])


# from alpha_vantage.timeseries import TimeSeries
# API_Key = 'J63G1AJ3FL74N43G'
# ts = TimeSeries(key = API_Key, output_format = 'pandas')
# data = ts.get_intraday('UJJIVANSFB.NS')
# data[0]

# from alpha_vantage.timeseries import TimeSeries
# ts = TimeSeries(key='J63G1AJ3FL74N43G', output_format='json')
# data, meta_data = ts.get_intraday(symbol='UJJIVANSFB.NS', interval='1min', outputsize='compact')
# print(data)

# import yfinance as yf
# stock = yf.Ticker("UJJIVANSFB.NS")
# data = stock.history(period="1d")
# print(f"Ujjivan Small Finance Bank last closing price: {data['Close'].iloc[-1]}")


# import yfinance as yf
# stock = yf.Ticker("UJJIVANSFB.NS")
# data = stock.history(period="max")
# print(data)

# import yfinance as yf
# import time
#Initialize the Ticker object for Ujjivan Small Finance Bank
# stock = yf.Ticker("UJJIVANSFB.NS")

# Infinite loop to fetch and display updated data every minute
# while True:
#     data = stock.history(period="1d", interval="1m")
#     print(data.tail())
#     # Save or process the data (e.g., compute risk metrics)
    
#     # Wait for 60 seconds before fetching new data
#     time.sleep(60)


# import yfinance as yf
# import matplotlib.pyplot as plt
# from datetime import datetime

# # Fetch stock data for today's intraday prices
# stock = yf.Ticker("UJJIVANSFB.NS")

# # Get today's data with 1-minute interval
# data = stock.history(period="1d", interval="1m")

# # Check if data is available
# if not data.empty:
#     # Extract time and close price for plotting
#     times = data.index
#     prices = data['Close']

#     # Plot today's stock price movement
#     plt.figure(figsize=(12, 6))
#     plt.plot(times, prices, linestyle='-', color='blue', marker='o', markersize=2)
#     plt.title("Ujjivan Small Finance Bank (Today’s Intraday Price Movement)")
#     plt.xlabel("Time")
#     plt.ylabel("Price (INR)")
#     plt.xticks(rotation=45)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
# else:
#     print("No data found for today's trading session.")


# import yfinance as yf
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime

# # Fetch stock data for Ujjivan Small Finance Bank
# stock = yf.Ticker("UJJIVANSFB.NS")

# # Set up the plot
# plt.ion()  # Turn on interactive mode
# fig, ax = plt.subplots(figsize=(12, 6))

# # Initialize lists to store time and prices for plotting
# times = []
# prices = []

# # Infinite loop to fetch and plot updated data every minute
# while True:
#     # Get today's data with 1-minute interval
#     data = stock.history(period="1d", interval="1m")
    
#     if not data.empty:
#         # Get the latest timestamp and price
#         last_time = data.index[-1]
#         last_price = data['Close'].iloc[-1]

#         # Add data to lists
#         times.append(last_time)
#         prices.append(last_price)

#         # Clear the plot and redraw with updated data
#         ax.clear()
#         ax.plot(times, prices, marker='o', linestyle='-', color='blue')
#         ax.set_title("Ujjivan Small Finance Bank (Today’s Intraday Price Movement)")
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Price (INR)")
#         plt.xticks(rotation=45)
#         ax.grid(True)
#         plt.tight_layout()
        
#         # Pause briefly before the next update
#         plt.pause(60)

#     else:
#         print("No data found for the current minute.")
    
#     # Wait for 60 seconds before fetching new data
#     time.sleep(60)


# import yfinance as yf
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime

# # Fetch stock data for Ujjivan Small Finance Bank
# stock = yf.Ticker("UJJIVANSFB.NS")

# # Set up the plot
# plt.ion()  # Turn on interactive mode
# fig, ax = plt.subplots(figsize=(12, 6))

# # Initialize lists to store time and prices for plotting
# times = []
# prices = []

# # Infinite loop to fetch and plot updated data every minute
# while True:
#     # Get today's data with 1-minute interval
#     data = stock.history(period="1d", interval="1m")
    
#     if not data.empty:
#         # Get the latest timestamp and price
#         last_time = data.index[-1]
#         last_price = data['Close'].iloc[-1]

#         # Add data to lists
#         times.append(last_time)
#         prices.append(last_price)

#         # Clear the plot and redraw with updated data
#         ax.clear()
#         ax.plot(times, prices, marker='o', linestyle='-', color='blue')
#         ax.set_title("Ujjivan Small Finance Bank (Today’s Intraday Price Movement)")
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Price (INR)")
#         plt.xticks(rotation=45)
#         ax.grid(True)
#         plt.tight_layout()

#         # Pause briefly before the next update
#         plt.pause(60)
    
#     else:
#         print("No data found for the current minute.")
    
#     # Wait for 60 seconds before fetching new data
#     time.sleep(60)


# import yfinance as yf
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime

# # Fetch stock data for Ujjivan Small Finance Bank
# stock = yf.Ticker("UJJIVANSFB.NS")

# # Set up the plot
# plt.ion()  # Turn on interactive mode
# fig, ax = plt.subplots(figsize=(12, 6))

# # Initialize lists to store time and prices for plotting
# times = []
# prices = []

# # Infinite loop to fetch and plot updated data every minute
# while True:
#     # Get today's data with 1-minute interval
#     data = stock.history(period="1d", interval="1m")
    
#     if not data.empty:
#         # Get the latest timestamp and price
#         last_time = data.index[-1]
#         last_price = data['Close'].iloc[-1]

#         # Add data to lists
#         times.append(last_time)
#         prices.append(last_price)

#         # Clear the plot and redraw with updated data
#         ax.plot(times, prices, marker='o', linestyle='-', color='blue')
#         ax.set_title("Ujjivan Small Finance Bank (Today’s Intraday Price Movement)")
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Price (INR)")
#         plt.xticks(rotation=45)
#         ax.grid(True)
#         plt.tight_layout()

#         # Pause briefly before the next update
#         plt.pause(60)
    
#     else:
#         print("No data found for the current minute.")
#     # Wait for 60 seconds before fetching new data
#     time.sleep(60)















