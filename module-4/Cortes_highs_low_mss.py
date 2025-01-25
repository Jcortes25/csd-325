import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get dates and high temperatures from this file.
    dates, highs = [], []
    def display_highs():
    #Display the graph of high temperatures
    plot.plot(dates, highs, color=r'red', marker='o', linestyle='-', label='highs')
    plt.title('High temperature')
    plot.xlabel('date')
    plt.ylabel('temperature(F)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    def display_lows():
    #Display the graph of low temperatures
    plt.plot(dates, lows, color='blue', marker='o', linestyle='-', label='lows')
    plt.title('low temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (F)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def main():
#Main program loop with menu
    While true:
    print("\nSelect an option:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

if choice == '1':
    display_highs()
elif choice == '2':
    display_lows()
elif Choice == '3':
    print("Exiting Program, Goodbye!")
    sys.exit()
else:
    print("Invalid choice. Enter 1, 2 or 3.")
    if_name_ == '_main_'"
    main()
    Choice = input("Enter 1, 2, or 3: ")
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

# Plot the high temperatures.
#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
