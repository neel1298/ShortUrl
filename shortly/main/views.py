from django.shortcuts import render,redirect,HttpResponseRedirect
from .shortner import shortner
from .models import shoryDB
# Create your views here.


def home(request):
    if request.method == 'POST':
        orignal_url = request.POST['urlname']
        mod_url = shortner().shorturl(orignal_url)

        newObject = shoryDB.objects.create(short_url=mod_url,long_url=orignal_url)
        newObject.save()

        return render(request,'home.html',{'content':mod_url})

    return render(request,'home.html')    


def gotoSite(request,st1):
    if shoryDB.objects.filter(short_url=st1).exists():
        urlObject = shoryDB.objects.filter(short_url=st1)[0]
        print("..............."+urlObject.long_url)
        return redirect(urlObject.long_url)

    return HttpResponseRedirect('www.google.co.in')    