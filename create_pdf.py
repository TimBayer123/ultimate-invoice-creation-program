from fpdf import FPDF
 
def create_PDF(invoice):
	pdf = FPDF(orientation='P', unit='mm', format='A5')
	pdf.add_page()
	pdf.set_font("Arial", style="B", size=12)
	pdf.cell(200, 10, txt="Rechnung", ln=2, align="C")
	pdf.set_font("Arial", style="I", size=12)
	pdf.cell(200, 10, txt="Rechnungsempfänger:" + invoice.receiver, ln=1, align="L")
	pdf.cell(200, 10, txt="Rechnungsdatum:" + invoice.invoice_date, ln=1, align="L")	
	pdf.cell(200, 10, txt="Preis netto:" + str(invoice.net_price), ln=1, align="L")	
	pdf.cell(200, 10, txt="Mwst. Satz:" + str(invoice.value_added_tax), ln=1, align="L")
	pdf.cell(200, 10, txt="Preis brutto:" + str(invoice.gross_price()), ln=1, align="L")
	pdf.cell(200, 10, txt="Vat-ID:" + invoice.vat_id, ln=1, align="L")
	# pdf.output("simple_Invoice.pdf")
	return pdf.output(dest='S').encode('latin-1')