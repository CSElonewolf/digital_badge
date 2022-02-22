from django import forms
from .models import Badge

class CreateBadgeForm(forms.ModelForm):
	badge_image = forms.ImageField(required=False,error_messages={'invalid':{"'Image files only"}}, widget = forms.FileInput)
	class Meta:
		model = Badge
		fields = ['name','badge_description','badge_image','email']

	def __init__(self,*args,**kwargs):
		super(CreateBadgeForm,self).__init__(*args,**kwargs)
		self.fields['name'].widget.attrs['placeholder'] = 'Badge Name'
		self.fields['badge_description'].widget.attrs['placeholder'] = 'Badge Description'
		self.fields['email'].widget.attrs['placeholder'] = 'Eligible Students'

		self.fields['badge_description'].widget.attrs['rows'] = 3
		self.fields['email'].widget.attrs['rows'] = 3

	# loop through all the fields and add class
		for field in self.fields:
			if field != 'badge_image':
				self.fields[field].widget.attrs['class'] = 'form-control'
			else:
				self.fields[field].widget.attrs['class'] = 'form-control-file'
				self.fields[field].widget.attrs['id'] = 'image_uploads"'
				self.fields[field].widget.attrs['accept'] = '.png'

