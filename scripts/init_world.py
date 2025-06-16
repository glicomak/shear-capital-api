import os
import uuid
import random
import json

INITIAL_POPULATION = 1000
NUM_INITIAL_OWN_UNITS = 500_000
NUM_INITIAL_SHARED_UNITS = 500_000

DATABASE_PATH = "../database"
TEMPLATE_PATH = "../templates"

tables = ["persons", "stocks"]
for table in tables:
    for file_name in os.listdir(f"{DATABASE_PATH}/{table}"):
        os.remove(f"../database/{table}/{file_name}")

def load_template(name):
    with open(f"{TEMPLATE_PATH}/{name}.txt", "r") as template_file:
        objects = [object.strip() for object in template_file.readlines()]
    return objects

first_names = load_template("first_names")
last_names = load_template("last_names")

person_id_circle = [str(uuid.uuid4()) for _ in range(INITIAL_POPULATION)]
stock_id_circle = [(str(uuid.uuid4()), str(uuid.uuid4())) for _ in range(INITIAL_POPULATION)]

for idx in range(INITIAL_POPULATION):
    own_stock_id = stock_id_circle[idx][0]
    own_stock = dict(
        id=own_stock_id,
        owner_id=person_id_circle[idx],
        person_id=person_id_circle[idx],
        units=NUM_INITIAL_OWN_UNITS
    )
    with open(f"{DATABASE_PATH}/stocks/{own_stock_id}.json", "w") as stock_file:
        json.dump(own_stock, stock_file, indent=4)
    
    shared_stock_id = stock_id_circle[idx][1]
    next_idx = (idx + 1) % INITIAL_POPULATION
    shared_stock = dict(
        id=shared_stock_id,
        owner_id=person_id_circle[idx],
        person_id=person_id_circle[next_idx],
        units=NUM_INITIAL_SHARED_UNITS
    )
    with open(f"{DATABASE_PATH}/stocks/{own_stock_id}.json", "w") as stock_file:
        json.dump(own_stock, stock_file, indent=4)

for idx in range(INITIAL_POPULATION):
    person_id = person_id_circle[idx]
    prev_idx = (idx + INITIAL_POPULATION - 1) % INITIAL_POPULATION
    person = dict(
        id=person_id,
        name=dict(first=random.choice(first_names), last=random.choice(last_names)),
        length=0,
        last_cut=0,
        owned_stocks=[stock_id_circle[idx][0], stock_id_circle[idx][1]],
        issued_stocks=[stock_id_circle[idx][0], stock_id_circle[prev_idx][1]]
    )
    with open(f"{DATABASE_PATH}/persons/{person_id}.json", "w") as person_file:
        json.dump(person, person_file, indent=4)
