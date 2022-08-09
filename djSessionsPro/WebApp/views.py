from django.shortcuts import render
# Create your views here.
def PageHitView(request):
    hit=request.session.get('hit',0)
    newhit=hit+1
    request.session['hit']=newhit
    print("Session Expired Age: ",request.session.get_expiry_age())
    print("Session Expired Date: ", request.session.get_expiry_date())
    return render(request,'MyApp/hits.html',{'hit':newhit})
