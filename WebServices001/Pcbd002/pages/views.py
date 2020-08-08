from django.shortcuts import render

# Create your views here.
def index(request):
    #    return HttpResponse('<h1>Hello CBD Work</h1>')
    return render (request, 'pages/index.html')



def about(request):
    #    return HttpResponse('<h1>Hello CBD Work</h1>')
    return render (request, 'pages/about.html')


def ML001(request):
    return render (request, 'pages/about.html')



def ML002(request):
    return render (request, 'pages/about.html')
