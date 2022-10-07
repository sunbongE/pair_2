from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def reviews(request):
    
    return render(request, 'reviews/reviews.html')

def create(request):
    return render(request, 'reviews/create.html')