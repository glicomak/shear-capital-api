import json

with open("meta/config.json", "r") as config_file:
    config = json.load(config_file)

POPULATION = config["population"]
NUM_STOCK_UNITS = config["num_stock_units"]

SECONDS_PER_DAY = config["seconds_per_day"]
START_TIMESTAMP = config["start_timestamp"]
