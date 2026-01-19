from django.contrib import admin
from .models import AboutUs, Category, Post




# Customize the admin interface for Post model
class postAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title','content')
    list_filter =('category','created_at')
# Register your models here.

admin.site.register(Post,postAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
