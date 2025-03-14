from django.contrib import admin
from .models import Contact, TodoItem
# Register your models here.

admin.site.register(Contact) #registering the Contact model with the admin site

admin.site.register(TodoItem) #registering the TodoItem model with the admin site
