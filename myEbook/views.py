from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
  feature1 = Feature()
  feature1.id = 0
  feature1.name = 'Yoyoyo'
  feature1.detail = 'Ulgo shipji anha'
  return render(request, 'index.html', {'feature': feature1})

def counter(request):
  text = request.GET['text']
  amount_of_words = len(text.split())
  return render(request, 'counter.html', {'amount': amount_of_words})