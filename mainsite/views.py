from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .models import Link
# Create your views here.
 
def scrape(request):
    if(request.method=="POST"):
        site= request.POST.get('site','')
        page=requests.get(site)
        soup=BeautifulSoup(page.text,'html.parser')

        for link in soup.find_all('a'):
            link_address=link.get('href')
            link_txt=link.string 
            Link.objects.create(address=link_address,name=link_txt)
        return HttpResponseRedirect('/')
    else:
        data=Link.objects.all()
    return render(request,'mainsite/result.html',{'links':data})

def delete(request):
    Link.objects.all().delete()
    return render(request,'mainsite/result.html')