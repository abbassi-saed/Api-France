from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

def list_houses(request):
    data = requests.get("http://api.cquest.org/dvf?section=94068000CQ").json()
    paginator = Paginator(data['resultats'],20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {'page_obj': page_obj})
