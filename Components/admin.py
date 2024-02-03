from django.contrib import admin
from .models import Passive

@admin.register(Passive)
class PassiveAdmin(admin.ModelAdmin):
    list_display = ['type','heading']

    fieldsets = [
        ('Main Information', {'fields': ['type','heading', 'background_image']}),
        ('Paragraphs and Images', {'fields': ['para1', 'image1', 'para2', 'h2', 'para3', 'image2']}),
    ]