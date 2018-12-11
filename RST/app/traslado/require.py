from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 

def renderPDF(plantilla,content={}):
	t=get_template(plantilla)
	send_data=t.render(content)
	result=BytesIO()
	pdf=pisa.pisaDocument(BytesIO(send_data.encode("ISO-8859-1")),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),content_type="application/pdf")
	else:
		return None

