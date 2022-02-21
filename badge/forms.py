from django import forms
from .models import Badge

class CreateBadgeForm(forms.ModelForm):
	class Meta:
		model = Badge
		fields = ['badge_name','badge_description','badge_image','eligible_students']

	def __init__(self,*args,**kwargs):
		super(CreateBadgeForm,self).__init__(*args,**kwargs)
		self.fields['badge_name'].widget.attrs['placeholder'] = 'Badge Name'
		self.fields['badge_description'].widget.attrs['placeholder'] = 'Badge Description'
		self.fields['eligible_students'].widget.attrs['placeholder'] = 'Eligible Students'

		self.fields['badge_description'].widget.attrs['rows'] = 3
		self.fields['eligible_students'].widget.attrs['rows'] = 3

	# loop through all the fields and add class
		for field in self.fields:
			if field != 'badge_image':
				self.fields[field].widget.attrs['class'] = 'form-control'
			else:
				self.fields[field].widget.attrs['class'] = 'form-control-file'

