import json
import os

from models import Person

class WorldCreator:
    def run(self):
        self._clear_tables()
        self._init_persons()
    
    def _clear_tables(self):
        tables = ["person", "stock"]
        for table in tables:
            for file_name in os.listdir(f"database/{table}"):
                os.remove(f"database/{table}/{file_name}")

    def _init_persons(self):
        with open("meta/config.json", "r") as config_file:
            config = json.load(config_file)

        for _ in range(config["population"]):
            person = Person.new()
            person.save()

creator = WorldCreator()
creator.run()
