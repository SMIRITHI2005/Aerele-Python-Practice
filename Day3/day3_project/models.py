from dataclasses import dataclass

@dataclass
class Invoice:

    invoice_id: str
    customer: str
    amount: float
    gst: float

    @property
    def total(self):
        return self.amount + self.gst