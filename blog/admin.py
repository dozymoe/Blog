from django.contrib import admin
from models import Post, Category
from django_markdown.admin import MarkdownModelAdmin


class PostAdmin(MarkdownModelAdmin):
    exclude = ('author', )
    list_display = ['title', 'author']
    search_fields = ['title', 'author']
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)