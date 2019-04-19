from django.shortcuts import render

# Create your views here.

def index(request):
    pass


def query(request):
    return render(request, 'engine/query.html', {})
