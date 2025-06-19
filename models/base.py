import json

class BaseModel:
    def save(self):
        with open(f"database/{self._model_name}/{self.id}.json", "w") as json_file:
            json.dump(self._to_dict(), json_file, indent=4)

    @classmethod
    def from_id(cls, id):
        with open(f"database/{cls._model_name}/{id}.json", "r") as json_file:
            data = json.load(json_file)
        return cls(**data)
