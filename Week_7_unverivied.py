import csv
import matplotlib.pyplot as plt

with open("titanic.csv") as f:
    reader = csv.reader(f)
    #Skip first line
    next(reader)

    count_passengers_in_age_range = 0
    #List of the ages in the specified range
    ages_in_fare_range = []
    #List of survivor count per class [Pclass1, Pclass2, Pclass3]
    survivor_counts_per_class = [0,0,0]

    #Read and store data
    for row in reader:
        if row[5] and 8 < float(row[5]) < 63:
            count_passengers_in_age_range += 1
        if 8 < float(row[9]) < 89 and row[5]:
            ages_in_fare_range.append(float(row[5]))
        if row[1] == "1":
            survivor_counts_per_class[int(row[2])-1] += 1

    #Average age of passengers with fare price between 8 and 89 and a known age
    print(round(sum(ages_in_fare_range)/len(ages_in_fare_range), 2))
    #Amount of passengers with an age between 8 and 63
    print(count_passengers_in_age_range)

    #Define graph characteristics
    x_ticks = ["1.Klasse", "2.Klasse", "3.Klasse"]
    colors = ["green", "red", "blue"]
    plt.bar(x_ticks, survivor_counts_per_class, color=colors)

    plt.title("Overlevingskans versus klasse aan boord van de Titanic")
    plt.xlabel("Passagierklasse")
    plt.ylabel("Aantal overlevende passagiers")

    plt.show()
