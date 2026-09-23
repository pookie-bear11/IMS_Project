from django.shortcuts import render
from .models import MovieAnime
# Create your views here.
def MovieAnime_list(request):
    products= MovieAnime.objects.all()

    context= {
        'MovieAnime': products
    }

    return render(request, 'InvApp/dashboard.html',context)
