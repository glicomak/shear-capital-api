import json
import os

class BaseModel:
    def save(self):
        with open(f"database/{self._model_name}/{self.id}.json", "w") as json_file:
            json.dump(self._to_dict(), json_file, indent=4)

    @classmethod
    def from_id(cls, id):
        with open(f"database/{cls._model_name}/{id}.json", "r") as json_file:
            data = json.load(json_file)
        return cls(**data)
    
    @classmethod
    def all(cls):
        all_objects = []

        for file_name in os.listdir(f"database/{cls._model_name}"):
            with open(f"database/{cls._model_name}/{file_name}", "r") as json_file:
                data = json.load(json_file)
                all_objects.append(cls(**data))

        return all_objects
