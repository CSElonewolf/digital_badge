from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages


from .forms import CreateBadgeForm
from .models import Badge

# Create your views here.
def create_badge(request):
	"""Create a badge """
	if request.method == "POST":
		form = CreateBadgeForm(request.POST,request.FILES)
		if form.is_valid():

			badge_name = form.cleaned_data['badge_name'].capitalize()
			badge_description = form.cleaned_data['badge_description']
			badge_image = form.cleaned_data['badge_image']
			eligible_students = form.cleaned_data['eligible_students'].lower()

			badge = Badge(badge_name = badge_name,badge_description=badge_description,badge_image = badge_image,eligible_students =eligible_students)
			badge.save()

		messages.success(request,'Badge has been created')

		return redirect('home')
	else:
		form = CreateBadgeForm()
		context = {
			'form':form
		}
		return render(request, 'badge/create_badge.html',context)

def verify_form(request):
	"""Display the verify form """
	return render(request,'badge/verfiy_form.html')

def verify(request):
	"""Check if the user is eligible for a batch or not"""
	name = None
	email = None
	if 'name' in request.GET:
		name = request.GET['name']
	if 'email' in request.GET:
		email = request.GET['email'].lower()

	if name is not None and email is not None:
		try:
			# check if the badge exists
			badge = get_object_or_404(Badge,badge_name=name.capitalize())
			emails = badge.eligible_students.split(',')
			# check if the email provided is eligible for the badge or not
			for email_value in emails:
				if email_value.find(email) != -1 and len(email_value) == len(email):

					response = JsonResponse({'status_code':200,'message':"student verified",'badge':badge.badge_image.url})
					return response
			# if email is associted with the badge doesnot exists 		#
			response = JsonResponse({'status_code':403})
			return response
		except:
			# if the badge doesnotexists
			response = JsonResponse({'status_code':403})
			return response
