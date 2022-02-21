from django.db import models

class Badge(models.Model):
	badge_name = models.CharField(max_length=50)
	badge_description = models.TextField(max_length=255)
	badge_image = models.ImageField(blank = True,upload_to='badges')
	eligible_students = models.TextField(max_length=255)
