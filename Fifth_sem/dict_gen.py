def generate_data(names, rates, bonuses):
    for i in range(len(names)):
        name = names[i]
        rate = rates[i]
        percentage = float(bonuses[i].strip('%'))
        bonus = int(rate * percentage/100)
        yield {name: rate + bonus}

names = ["Alice", "Bob", "Charlie"]
rates = [1000, 1500, 1200]
bonuses = ["10.25%", "8.5%", "12.75%"]

for data in generate_data(names, rates, bonuses):
    print(data)