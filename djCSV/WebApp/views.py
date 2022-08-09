from django.http import HttpResponse
import csv
def DownLoadCsvFile(request):
    x=HttpResponse(content_type='text/csv')
    x['Content-Disposition'] = 'attachment; filename="Rudra.csv"'
    y=csv.writer(x)
    y.writerow(['1001','SARA','Thomus','Network-Engineer'])
    y.writerow(['1002', 'DANIEL', 'RAJU', 'Software-Engineer'])
    y.writerow(['1003', 'SMITH', 'AMY', 'TestEngineer'])
    y.writerow(['1004', 'SCOTT', 'BEN', 'Developer'])
    y.writerow(['1005', 'Raju', 'Sir', 'DjangoEngineer'])
    return x
