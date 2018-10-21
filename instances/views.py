from django.shortcuts import render
from django.shortcuts import HttpResponse
from instances import models
# Create your views here.


#显示首页
def index(request):
    context = {}
    return render(request, 'index.html', context)
