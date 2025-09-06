from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tags","date")
    list_display = ("title","date","author")
    prepopulated_fields = {"slug":("title",)}


admin.site.register(models.Author)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Tag)
