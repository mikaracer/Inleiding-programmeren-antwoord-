import csv
import matplotlib.pyplot as plt

def average_age_in_fare_range(filename, fare_min, fare_max):
    """Calculates the average age in a fare range."""
    ages = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        for i, row in enumerate(reader, start=2):
            try:
                if row[9] and fare_min < float(row[9]) < fare_max and row[5]:
                    ages.append(float(row[5]))
            except (IndexError, ValueError):
                print(f'Invalid age or fare value on line {i}: {row}')
                continue

        return round(sum(ages) / len(ages), 2)


def count_passengers_in_age_range(filename, age_min, age_max):
    """Counts the number of passengers in an age range."""
    count = 0
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        for i, row in enumerate(reader, start=2):
            try:
                if row[5] and age_min < float(row[5]) < age_max:
                    count += 1
            except (IndexError, ValueError):
                print(f'Invalid age value on line {i}: {row}')
                continue
        return count


def plot_survivors_by_class(filename):
    """Plots the survivor counts for each class."""
    survivor_counts_per_class = [0,0,0]
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        for i, row in enumerate(reader, start=2):
            try:
                if row[1] == "1":
                    survivor_counts_per_class[int(row[2])-1] += 1
            except (IndexError, ValueError):
                print(f'Invalid "survived" or class value on line {i}: {row}')
                continue

        #Define graph characteristics
        x_ticks = ["1.Klasse", "2.Klasse", "3.Klasse"]
        colors = ["green", "red", "blue"]
        plt.bar(x_ticks, survivor_counts_per_class, color=colors)

        plt.title("Overlevingskans versus klasse aan boord van de Titanic")
        plt.xlabel("Passagierklasse")
        plt.ylabel("Aantal overlevende passagiers")

        plt.show()
