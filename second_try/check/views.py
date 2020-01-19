from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def printin(request):
    #return HttpResponse("Hello Good Luck")
    return render(request,"first_view_first_app.html")