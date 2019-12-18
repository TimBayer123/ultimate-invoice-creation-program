
from datetime import date
from vat_validation import check_vat

class Invoice:

    def __init__(self, receiver, net_price, invoice_date = date.today(), vat_id = None, value_added_tax = 0.19):
        self.receiver = receiver
        self.net_price = net_price
        self.invoice_date = invoice_date
        self.vat_id = vat_id
        self.value_added_tax = value_added_tax

    def gross_price(self):
        return self.net_price * (1 + self.value_added_tax)

    def apply_vat_regulation(self):
        if(check_vat(self.vat_id)):
            self.value_added_tax = 0.0