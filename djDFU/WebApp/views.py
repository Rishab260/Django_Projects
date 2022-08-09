from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def FileUpload(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        x=fs.url(filename)
        return render(request,'MyApp/welcome.html',{'x':x})
    return render(request,'MyApp/welcome.html')