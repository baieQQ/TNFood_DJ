from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello food!")
    return render(request, 'food/index.html',{'place_nums': range(6)})