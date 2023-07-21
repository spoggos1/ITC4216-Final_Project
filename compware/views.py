from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.
def index(request):
        mydata = list(Item.objects.all())
        template = loader.get_template('compware/index.html')
        context = {
            'Item': mydata,
        }
        return HttpResponse(template.render(context,request))
    

def about(request):
    return render(request, 'compware/about.html')

