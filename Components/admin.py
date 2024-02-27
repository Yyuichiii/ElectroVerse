from django.contrib import admin
from .models import Component,Product
from django_summernote.admin import SummernoteModelAdmin




@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['Category','Type']
    search_fields = ['Category', 'Type', 'heading']
    list_filter = ['Category']
    fieldsets = [
        ('Main Information', {'fields': ['Category','Type','heading', 'background_image']}),
        ('Paragraphs and Images', {'fields': ['content1', 'image1','content2', 'image2','content3', 'image3','content4', 'image4','content5', 'image5',]}),
    ]   

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('P_name','Type', 'Bundle_set', 'Price',)
    search_fields = ['Type','P_name',]
    list_filter = ['Bundle_set', 'Price']
    fieldsets = [
        ('Main Information (Important)', {'fields': ['Type','P_name', 'Bundle_set', 'Price','P_image']}),
        ('Paragraphs and Images', {'fields': ['background_image','content',]}),
    ]
  

admin.site.register(Product, ProductAdmin) 