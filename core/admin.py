from django.contrib import admin
from .models import Registration, Investment, Member, Transaction, Leaver

# Register your models here.
admin.site.register(Registration)
admin.site.register(Investment)
admin.site.register(Member)
admin.site.register(Transaction)
admin.site.register(Leaver)
