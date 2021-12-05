from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import Filter

def list_houses(request):
    api = "http://api.cquest.org/dvf?"
    val = request.POST
    for k, v in val.items():
        if v and not k == "csrfmiddlewaretoken":
            print(k)
            api=f"{api}{k}={v}&"
    print(api)
    apiUrl = f"http://api.cquest.org/dvf?code_commune=89304"
    data = requests.get(api).json()
    if not data.get("erreur"):
        paginator = Paginator(data['resultats'], 50000000000)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        moy = page_obj.valeur_fonciere / page_obj.surface_relle_bati
        return render(request, "index2.html", {'page_obj': page_obj, 'moy': moy, 'form': val.dict()})
    return render(request, "index2.html")