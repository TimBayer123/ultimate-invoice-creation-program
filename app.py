# from datetime import strptime
from invoice import Invoice
from flask import Flask, request, make_response
from create_pdf import create_PDF

app = Flask(__name__)

def check_parameter_string_empty(raw_string):
    if len(raw_string) == 0:
        return 'parameter is empty', 500

@app.route('/invoice/create', methods=['POST'])
def invoice_create():
    raw_receiver = ''
    raw_date = ''
    raw_net_price = ''
    raw_tax = ''
    raw_vat_id = ''

    try:
        raw_receiver = request.form.get('receiver')
        raw_date = request.form.get('date')
        raw_net_price = request.form.get('net')
        raw_tax = request.form.get('tax')
        raw_vat_id = request.form.get('vatid')
    except ValueError:
        return 'parameter is missing', 500
    
    check_parameter_string_empty(raw_receiver)
    check_parameter_string_empty(raw_date)
    check_parameter_string_empty(raw_net_price)
    check_parameter_string_empty(raw_tax)
    check_parameter_string_empty(raw_vat_id)

    net_price = float(raw_net_price)
    value_added_tax = float(raw_tax)
    invoice_date = raw_date
    receiver = raw_receiver
    vat_id = raw_vat_id

    invoice = Invoice(receiver, net_price, invoice_date=invoice_date, vat_id=vat_id, value_added_tax=value_added_tax)
    invoice.apply_vat_regulation()

    response = make_response(create_PDF(invoice))
    response.headers.set('Content-Disposition', 'attachment', filename='invoice' + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response
    

if __name__ == '__main__':
    app.run()
