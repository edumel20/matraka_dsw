from django.contrib import admin

from .models import Reason


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('post', 'label', 'labelled_because')
