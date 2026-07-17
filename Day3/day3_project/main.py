from models import Invoice
from controller import InvoiceController
from utils import calculate_gst

gst = calculate_gst(5000)

invoice = Invoice(

    invoice_id="INV001",
    customer="ABC Pvt Ltd",
    amount=5000,
    gst=gst
)

controller = InvoiceController(invoice)

controller.save()

controller.submit()

print(invoice)

print("Total =", invoice.total)