from django.shortcuts import render
# from django.template import loader
import datetime as dt
# from .models import Image


# Create your views here.
def index(request):
    return render(request, 'index.html')

def index(request):
    date = dt.date.today()
    # images = Image.get_images()
    return render(request, 'index.html', {"date": date,})
