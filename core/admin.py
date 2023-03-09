from django.contrib import admin
from .models import Registration, Investment, Member

# Register your models here.
admin.site.register(Registration)
admin.site.register(Investment)
admin.site.register(Member)
