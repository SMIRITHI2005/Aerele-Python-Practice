from database import database

class InvoiceController:

    def __init__(self, invoice):

        self.invoice = invoice

    def validate(self):

        if self.invoice.amount <= 0:
            raise ValueError("Amount should be positive")

        if self.invoice.customer == "":
            raise ValueError("Customer name required")

    def before_save(self):

        print("Preparing Invoice...")

    def save(self):

        self.validate()

        self.before_save()

        database.append(self.invoice)

        print("Invoice Saved")

    def submit(self):

        print("Invoice Submitted")