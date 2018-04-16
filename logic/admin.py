from django.contrib import admin

# Register your models here.
from logic.models import Kweet, Profile

admin.site.register(Kweet)
admin.site.register(Profile)
