from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import SentForm
# Create your views here.
def SendingMail(request):
    if request.method == 'POST':
        form=SentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            mail=form.cleaned_data['mail']
            sub=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail('got mail from'+str(mail),
                      "name: "+str(name)+"\n"
                      "mail:"+str(mail)+"\n"
                      "subject:"+str(sub)+"\n"
                      "message:"+str(message),
                      settings.EMAIL_HOST_USER,
                      ['ksrajupy@gmail.com'],
                      fail_silently=False)
            return HttpResponseRedirect('/thanks')
    else:
        form=SentForm()
    return render(request,"MyApp/email.html",{'form':form})
def Thanks(request):
    return render(request,"MyApp/thanks.html")

