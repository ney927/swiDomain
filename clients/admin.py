from django.contrib import admin
from .models import client, industryChoices, positionChoices
# Register your models here.
admin.site.register(client),
admin.site.register(industryChoices),
admin.site.register(positionChoices)
