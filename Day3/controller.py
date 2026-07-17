class InvoiceController:

    def __init__(self, invoice):
        self.invoice = invoice

    def validate(self):
        if self.invoice.amount <= 0:
            raise ValueError("Invoice amount must be greater than zero")

        if self.invoice.tax < 0:
            raise ValueError("Tax cannot be negative")

        print("Invoice validation successful")

    def before_save(self):
        print("Preparing invoice before saving...")

    def save(self):
        self.validate()
        self.before_save()
        print("Invoice saved successfully")
        
invoice = Invoice(
    invoice_no="INV-001",
    customer="ABC Pvt Ltd",
    amount=1000,
    tax=180
)

controller = InvoiceController(invoice)
controller.save()