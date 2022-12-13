from django.shortcuts import render
from .models import productMainModel
# Create your views here.
def homepage(request):
    return render (request,'homepage.html')

def fetching_data(request):
    product=productMainModel.objects.all().values()
    return render(request,'homepage.html')


def get_by_id(request,id):
    product=productMainModel.objects.get(id=id)
    return render(request,'homepage.html')
