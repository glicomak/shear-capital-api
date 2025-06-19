import random

class Template:
    def __init__(self, name):
        self._options = []
        with open(f"templates/{name}.txt", "r") as text_file:
            self._options = [line.strip() for line in text_file.readlines()]
    
    def random(self):
        return random.choice(self._options)

first_names = Template("first_names")
last_names = Template("last_names")
