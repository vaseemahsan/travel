

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Symbol
from . models import Meettheteam


# Create your views here.
def index(request):
    obj=Place.objects.all()
    obj1=Meettheteam.objects.all()
    obj2=Symbol.objects.all()

    return render(request, 'index.html',{'results':obj,'teams':obj1,'sym':obj2})



#
# def about(request):
#     return render(request, 'about.html')
#
#
# def contact(request):
#     return HttpResponse('contact: 95805730740')
#
#
# def details(request):
#     return HttpResponse('Stay tuned')
#
#
# def thanks(request):
#     return HttpResponse('Thank you')
