from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.

# 后台优化
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tag, TagAdmin)