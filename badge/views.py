from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import CreateBadgeForm
from .models import Badge

# Create your views here.
def create_badge(request):
	if request.method == "POST":
		form = CreateBadgeForm(request.POST,request.FILES)
		if form.is_valid():

			badge_name = form.cleaned_data['badge_name']
			badge_description = form.cleaned_data['badge_description']
			badge_image = form.cleaned_data['badge_image']
			eligible_students = form.cleaned_data['eligible_students']

			badge = Badge(badge_name = badge_name,badge_description=badge_description,badge_image = badge_image,eligible_students =eligible_students)
			badge.save()
		messages.success(request,'Badge has been created')
		return redirect('home')
	else:
		form = CreateBadgeForm()
		context = {
			'form':form
		}
		return render(request, 'digital_badge/create_badge.html',context)
