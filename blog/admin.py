from django.contrib import admin
from .models import Post, Comment, Contact
from tinymce.widgets import TinyMCE
from django.db import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()}
    }

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'active')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
