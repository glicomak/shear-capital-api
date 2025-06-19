from core.config import NUM_STOCK_UNITS
from models import BaseModel
from uuid import uuid4

class Stock(BaseModel):
    _model_name = "stock"

    def __init__(self, id, owner_id, person_id, units):
        self.id = id
        self.owner_id = owner_id
        self.person_id = person_id
        self.units = units

    @classmethod
    def new(cls, person_id):
        return cls(
            id=str(uuid4()),
            owner_id=person_id,
            person_id=person_id,
            units=NUM_STOCK_UNITS
        )

    def _to_dict(self):
        return dict(
            id=self.id,
            owner_id=self.owner_id,
            person_id=self.person_id,
            units=self.units
        )
