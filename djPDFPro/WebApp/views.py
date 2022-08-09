from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.
def GetPDF(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="PyData.pdf"'
    Can=canvas.Canvas(response)
    Can.setFont('Times-Roman',55)
    Can.drawString(100,700,"Hei Django....!!")
    Can.showPage()
    Can.save()
    return response