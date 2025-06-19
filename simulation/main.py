from core.day import advance_day, current_day, target_day
from models.person import Person
from tqdm import tqdm

class Simulator:
    def run(self):
        persons = Person.all()

        start_day = current_day() + 1
        end_day = target_day() + 1

        if start_day == end_day:
            print("Simulation upto date")
            return

        print(f"Simulating from day {start_day} to {end_day - 1} ...")

        for _ in tqdm(range(start_day, end_day)):
            for person in persons:
                person.simulate()
            advance_day()
        
        for person in persons:
            person.save()

simulator = Simulator()
simulator.run()
