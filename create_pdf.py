from fpdf import FPDF
 
def create_PDF():
	pdf = FPDF(orientation='P', unit='mm', format='A5')
	pdf.add_page()
	pdf.set_font("Arial", style="B", size=12)
	pdf.cell(200, 10, txt="Rechnung", ln=2, align="C")
	pdf.set_font("Arial", style="I", size=12)
	pdf.cell(200, 10, txt="Rechnungsempfänger:", ln=1, align="L")
	pdf.cell(200, 10, txt="Rechnungsdatum:", ln=1, align="L")	
	pdf.cell(200, 10, txt="Preis netto:", ln=1, align="L")	
	pdf.cell(200, 10, txt="Mwst. Satz:", ln=1, align="L")
	pdf.cell(200, 10, txt="Preis brutto:", ln=1, align="L")
	pdf.cell(200, 10, txt="Vat-ID:", ln=1, align="L")
	pdf.output("simple_Invoice.pdf")