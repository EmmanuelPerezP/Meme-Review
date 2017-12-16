from django.contrib import admin
from .models import Image, Meme, Review


# Register your models here.
admin.site.register(Image)
admin.site.register(Meme)
admin.site.register(Review)
