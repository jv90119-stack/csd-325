import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

def read_weather_data(filename):
    """Read dates, high, and low temperatures from a CSV file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {row[2]}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows

def plot_data(dates, temps, label, color):
    """Plot temperature data with given label and color."""
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(f"Daily {label} Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)

    print("\n  Welcome to the Sitka Weather Data Viewer ️")
    print("------------------------------------------------")
    print("Instructions:")
    print("Type 'highs' to view daily high temperatures.")
    print("Type 'lows' to view daily low temperatures.")
    print("Type 'exit' to quit the program.")
    print("------------------------------------------------")

    while True:
        choice = input("\nEnter your choice (highs/lows/exit): ").strip().lower()

        if choice == 'highs':
            print("Displaying high temperature graph...")
            plot_data(dates, highs, "High", 'red')
        elif choice == 'lows':
            print("Displaying low temperature graph...")
            plot_data(dates, lows, "Low", 'blue')
        elif choice == 'exit':
            print("\nThank you for using the Sitka Weather Data Viewer. ")
            sys.exit()
        else:
            print("Invalid choice. Please enter 'highs', 'lows', or 'exit'.")

if __name__ == '__main__':
    main()
