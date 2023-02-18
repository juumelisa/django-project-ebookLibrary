from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context = {
    'name': 'Seungcheol',
    'age': 28
  }
  return render(request, 'index.html', context)
