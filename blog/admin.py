"""configuration for django.contrib.admin"""

from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import Post, Category


class PostAdmin(MarkdownModelAdmin):
    """django admin configuration for the Post model"""

    exclude = ('author', )
    list_display = ['title', 'author']
    search_fields = ['title', 'author']
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    """django admin configuration for the Category model"""

    list_display = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
