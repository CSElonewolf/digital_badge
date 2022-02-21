from django.contrib import admin
from django.utils.html import format_html
from .models import Badge

class BadgeAdmin(admin.ModelAdmin):
	list_display = ('thumbnail','badge_name')
	list_display_links = ('thumbnail','badge_name')

	def thumbnail(self,object):
		return format_html('<img src="{}" width="40" height="40" style="border-radius:50%;">'.format(object.badge_image.url))

	thumbnail.short_description = 'Badge Image'


admin.site.register(Badge,BadgeAdmin)