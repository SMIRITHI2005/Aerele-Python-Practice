from dataclasses import dataclass

@dataclass
class Invoice:
    invoice_no: str
    customer: str
    amount: float
    tax: float

    @property
    def total(self):
        return self.amount + self.tax


invoice = Invoice(
    invoice_no="INV-001",
    customer="ABC Pvt Ltd",
    amount=1000,
    tax=180
)

print(invoice)
print("Total:", invoice.total)

