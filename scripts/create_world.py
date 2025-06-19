import os

from core.config import POPULATION
from models import Person

class WorldCreator:
    def run(self):
        self._clear_tables()
        self._reset_meta()
        self._init_persons()
    
    def _clear_tables(self):
        tables = ["person", "stock"]
        for table in tables:
            for file_name in os.listdir(f"database/{table}"):
                os.remove(f"database/{table}/{file_name}")
    
    def _reset_meta(self):
        with open("meta/day.txt", "w") as day_file:
            day_file.write(str(0))

    def _init_persons(self):
        for _ in range(POPULATION):
            person = Person.new()
            person.save()

creator = WorldCreator()
creator.run()
