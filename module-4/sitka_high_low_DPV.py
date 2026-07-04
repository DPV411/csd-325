import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates = []
    highs = []
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Plot the high temperatures.
#plt.style.use('seaborn')
#fig, ax = plt.subplots()
#ax.plot(dates, highs, c='red')

# Format plot.
#plt.title("Daily high temperatures - 2018", fontsize=24)
#plt.xlabel('', fontsize=16)
#fig.autofmt_xdate()
#plt.ylabel("Temperature (F)", fontsize=16)
#plt.tick_params(axis='both', which='major', labelsize=16)

#plt.show()
choice = ""
while choice != "3":
    print("\nWeather Menu")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
       fig, ax = plt.subplots()
       ax.plot(dates, highs, c='red')
       
       plt.title("Daily high temperatures - 2018", fontsize=24)
       plt.xlabel("",fontsize=16)
       fig.autofmt_xdate()
       plt.ylabel("Temperature (F)", fontsize=16)
       plt.tick_params(axis="both", which="major", labelsize=16)
       
       plt.show()
    elif choice == "2":
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel("",fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis="both", which="major", labelsize=16)

        plt.show()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")