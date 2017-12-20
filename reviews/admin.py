from django.contrib import admin
from .models import Image, Meme, Review


# Register your models here.
admin.site.register(Image)
# admin.site.register(Meme)


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Review)
