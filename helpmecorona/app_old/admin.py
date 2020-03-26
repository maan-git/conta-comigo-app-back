from django.contrib import admin

from .models import Post, Person, Address

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Address)

# Register your models here.
