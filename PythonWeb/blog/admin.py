from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter =['date']
    search_fields = ['title']
    inlines = [CommentInLine]

admin.site.register(Post, PostAdmin)