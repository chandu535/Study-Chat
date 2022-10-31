from email import message
from django.contrib import admin

from base.views import room

# Register your models here.

from .models import Room, Topic, Message, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)