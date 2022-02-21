from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def create_badge(request):
	return render(request, 'digital_badge/create_badge.html')