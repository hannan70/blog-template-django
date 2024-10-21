from django.contrib import admin
from .models import Post, Comment, Tag, Author, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['post_title']}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Category)
