from django.contrib import admin
from .models import AboutUs, Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("category",)


admin.site.register(Category)
admin.site.register(AboutUs)
