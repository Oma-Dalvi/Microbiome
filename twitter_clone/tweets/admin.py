from django.contrib import admin
from .models import *

admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Share)