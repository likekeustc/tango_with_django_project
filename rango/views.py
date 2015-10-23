from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)
#    return HttpResponse("Rango says hey there world!")

def about(request):
    context_dict = {'boldmessage': "Odin provides point of sales solutions."}
    return render(request, 'rango/about.html', context_dict)

