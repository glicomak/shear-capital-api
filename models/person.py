import random

from core.day import current_day
from core.templates import first_names, last_names
from models import BaseModel, Stock
from utils.math import clipped_normal
from uuid import uuid4

class Person(BaseModel):
    _model_name = "person"

    def __init__(self, id, name, genetics, length, history, owned_stocks, issued_stocks):
        self.id = id
        self.name = name
        self.length_genetics = genetics["length"]
        self.color_genetics = genetics["color"]
        self.length = length
        self.history = history
        self.owned_stocks = owned_stocks
        self.issued_stocks = issued_stocks

    @classmethod
    def new(cls):
        person_id = str(uuid4())

        stock = Stock.new(person_id)
        stock.save()

        return cls(
            id=person_id,
            name=[first_names.random(), last_names.random()],
            genetics=dict(
                length=dict(
                    mean=clipped_normal(0.05, 0.006, 0.02),
                    stdev=clipped_normal(0.002, 0.0003, 0.001)
                ),
                color="black"
            ),
            length=0,
            history=[dict(
                day=0,
                start_length=0,
                end_length=0
            )],
            owned_stocks=[stock.id],
            issued_stocks=[stock.id]
        )

    def simulate(self):
        self._grow()
        self._try_forced_cut()

    def _grow(self):
        params = self.length_genetics
        self.length += clipped_normal(params["mean"], params["stdev"])
        self.length = round(self.length, 6)
    
    def _try_forced_cut(self):
        if random.random() < self._prob_forced_cut_today():
            old_length = self.length
            self.length = round(self.length * random.random(), 6)

            self.history.append(dict(
                day=current_day(),
                start_length=old_length,
                end_length=self.length
            ))
    
    def _prob_forced_cut_today(self):
        alpha = 60
        beta = 2.5

        last_cut = self.history[-1]["day"]
        t = current_day() - last_cut

        numerator = (beta / alpha) * (t / alpha) ** (beta - 1)
        denominator = 1 + (t / alpha) ** beta

        return numerator / denominator

    def _to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            genetics=dict(
                length=self.length_genetics,
                color=self.color_genetics
            ),
            length=self.length,
            history=self.history,
            owned_stocks=self.owned_stocks,
            issued_stocks=self.issued_stocks
        )
