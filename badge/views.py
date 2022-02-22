from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

# imports for building the rest api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# imports from the project
from .forms import CreateBadgeForm
from .models import Badge
from .serializers import BadgeSerializer


# Create your views here.
def create_badge(request):
	"""Create a badge """
	if request.method == "POST":
		form = CreateBadgeForm(request.POST,request.FILES)
		if form.is_valid():

			name = form.cleaned_data['name'].capitalize()
			badge_description = form.cleaned_data['badge_description']
			badge_image = form.cleaned_data['badge_image']
			email = form.cleaned_data['email'].lower()

			badge = Badge(name = name,badge_description=badge_description,badge_image = badge_image,email =email)
			badge.save()

		messages.success(request,'Badge has been created')

		return redirect('home')
	else:
		form = CreateBadgeForm()
		context = {
			'form':form
		}
		return render(request, 'badge/create_badge.html',context)

# def verify_form(request):
# 	"""Display the verify form """
# 	return render(request,'badge/verfiy_form.html')

# def verify(request):
# 	"""Check if the user is eligible for a batch or not"""
# 	name = None
# 	email = None
# 	if 'name' in request.GET:
# 		name = request.GET['name']
# 	if 'email' in request.GET:
# 		email = request.GET['email'].lower()

# 	if name is not None and email is not None:
# 		try:
# 			# check if the badge exists
# 			badge = get_object_or_404(Badge,name=name.capitalize())
# 			emails = badge.email.split(',')
# 			# check if the email provided is eligible for the badge or not
# 			for email_value in emails:
# 				if email_value.find(email) != -1 and len(email_value) == len(email):

# 					response = JsonResponse({'status_code':200,'message':"student verified",'badge':badge.badge_image.url})
# 					return response
# 			# if email is associted with the badge doesnot exists 		#
# 			response = JsonResponse({'status_code':403})
# 			return response
# 		except:
# 			# if the badge doesnotexists
# 			response = JsonResponse({'status_code':403})
# 			return response

def edit_badge(request,pk):
	badge = get_object_or_404(Badge,pk=pk)
	if request.method == "POST":
		badge_form = CreateBadgeForm(request.POST,request.FILES,instance = badge)
		if badge_form.is_valid():
			badge_form.save()
			messages.add_message(request,messages.SUCCESS,'Your badge has been updated!')
			return redirect('home')
	else:
		badge_form = CreateBadgeForm(instance = badge)
	context={
		'badge':badge,
		'form':badge_form,
	}
	return render(request, 'badge/edit_badge.html',context)

def delete_badge(request,pk):
	"""Deletes teh badge"""
	badge = get_object_or_404(Badge,pk=pk)
	badge.delete()
	messages.add_message(request,messages.ERROR,'Your badge has been deleted!')
	return redirect('home')


class VerifyBadge(APIView):
	"""Global API to verify if the student is eligible for the badge"""
	def get(self,request):
		try:
			name= request.GET['name']
			email = request.GET['email']
			badge =  Badge.objects.filter(name=name).filter(email__contains=email)
			serializer = BadgeSerializer(badge,many=True)
			return Response(serializer.data,status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_403_FORBIDDEN)

