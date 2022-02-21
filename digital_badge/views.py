from django.shortcuts import render
from badge.models import Badge

def home(request):
	"""Displaiy all the badges inside the database"""
	badges = None
	badges = Badge.objects.all()
	count = badges.count()
	context = {
		'badges':badges,
		'count':count,
	}
	return render(request, 'home.html',context)

