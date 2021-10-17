from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import Filter

def list_houses(request):

    val = request.POST.dict()
    print(val)
    test =  request.POST.get("code_commune")
    apiUrl = f"http://api.cquest.org/dvf?code_commune=89304"
    for k, v in val.items():
        apiUrl =f"?{k}={v}".join(apiUrl)
    print(apiUrl)
    data = requests.get(apiUrl).json()
    paginator = Paginator(data['resultats'], 20000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index2.html", {'page_obj': page_obj,'form':Filter})