from django.contrib import admin
from .models import Category, Post
from django_markdown.admin import MarkdownModelAdmin


class PostAdmin(MarkdownModelAdmin):
    exclude = ['author', 'slug']
    list_display = ['title', 'author']
    search_fields = ['title', 'author']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
