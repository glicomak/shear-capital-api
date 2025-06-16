import os
import json
import random

DAYS = 365

def cut_probability(t, alpha=60, beta=2.5):
    numerator = (beta / alpha) * (t / alpha) ** (beta - 1)
    denominator = 1 + (t / alpha) ** beta
    return numerator / denominator

def today_growth(mean=0.04, std_dev=0.01):
    return max(0.0, random.gauss(mean, std_dev))

for day in range(DAYS):
    for file_name in os.listdir("persons"):
        with open(f"persons/{file_name}", "r") as person_file:
            person = json.load(person_file)
        
        if random.random() < cut_probability(person["last_cut"]):
            person["length"] *= random.random()
            person["last_cut"] = 0
        else:
            person["length"] += today_growth()
            person["last_cut"] += 1
        
        if person["id"] == "db411008-71b6-4916-a3b6-05208b87dc40":
            print(f"Day {day}: {person['length']:.5f} cm")

        with open(f"persons/{file_name}", "w") as person_file:
            json.dump(person, person_file, indent=4)
