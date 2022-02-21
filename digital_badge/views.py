from django.shortcuts import render
from badge.models import Badge

def home(request):
	badges = None
	emails = []
	badges = Badge.objects.all()
	context = {
		'badges':badges,
	}
	return render(request, 'home.html',context)

