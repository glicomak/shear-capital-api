import random

from models import BaseModel, Stock
from uuid import uuid4

class Person(BaseModel):
    _model_name = "person"

    def __init__(self, id, name, genetics, length, last_cut, owned_stocks, issued_stocks):
        self.id = id
        self.name = name
        self.length_genetics = genetics["length"]
        self.color_genetics = genetics["color"]
        self.length = length
        self.last_cut = last_cut
        self.owned_stocks = owned_stocks
        self.issued_stocks = issued_stocks

    def grow_one_day(self):
        params = self.length_genetics
        self.length += max(0, random.gauss(params["mean"], params["stdev"]))

    @classmethod
    def new(cls):
        person_id = str(uuid4())

        stock = Stock.new(person_id)
        stock.save()

        return cls(
            id=person_id,
            name=["Hello", "World"],
            genetics=dict(
                length=dict(
                    mean=0,
                    stdev=0
                ),
                color="black"
            ),
            length=0,
            last_cut=0,
            owned_stocks=[stock.id],
            issued_stocks=[stock.id]
        )

    def _to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            genetics=dict(
                length=self.length_genetics,
                color=self.color_genetics
            ),
            length=self.length,
            last_cut=self.last_cut,
            owned_stocks=self.owned_stocks,
            issued_stocks=self.issued_stocks
        )
