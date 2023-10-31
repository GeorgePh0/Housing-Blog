from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    list_display = ('name', 'body', 'approved', 'created_on', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):

        queryset.update(approved=True)


admin.site.register(Profile)
