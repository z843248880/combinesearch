from django.contrib import admin

# Register your models here.

from combinesearchapp import models

admin.site.register(models.Direction)
admin.site.register(models.Classification)
admin.site.register(models.Video)
