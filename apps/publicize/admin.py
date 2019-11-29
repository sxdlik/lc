from django.contrib import admin

from .import models

admin.site.register(models.FlowPath)
admin.site.register(models.Step)
