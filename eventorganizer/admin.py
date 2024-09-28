from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models.organizers import Organizers
from .models.events import Events
from .models.customers import Customers
from .models.users import Users

class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'location')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        user, created = Users.objects.get_or_create(username=obj.email, defaults={
                'password': make_password('default_password'),
                'role': Users.ORGANIZER
            })

        if not created:
            user.role = Users.ORGANIZER
            user.save()

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'theme', 'organizer')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.organizer:
            obj.organizer = obj.organizer
            obj.save()

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'location', 'gender', 'event')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.event:
            obj.event = obj.event
            obj.save()

        user, created = Users.objects.get_or_create(username=obj.email, defaults={
                'password': make_password('default_password'),
                'role': Users.CUSTOMER
            })

        if not created:
            user.role = Users.CUSTOMER
            user.save()

# Register your models here.
admin.site.register(Organizers, OrganizerAdmin)
admin.site.register(Events, EventAdmin)
admin.site.register(Customers, CustomerAdmin)
admin.site.register(Users)