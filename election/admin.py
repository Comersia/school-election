from django.contrib import admin
from .models import Profile, Candidat, Vote, Election


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('username', 'form')
	list_filter = ('form', )
	search_fields = ('form__startswith',)

	def username(self, obj):
		return obj.user.username

admin.site.register([Candidat, Vote, Election])
# Register your models here.
