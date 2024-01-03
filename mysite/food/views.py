from django.shortcuts import render
from .models import Place

# Create your views here.
def index(request):
    # return HttpResponse("Hello food!")
    return render(request, 'food/index.html', {'store_list': Place.objects.all(), })