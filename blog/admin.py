from django.contrib import admin
from .models import Post, Comment, Scam
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'categorie', 'status', 'created_on')
    search_fields = ['tittle', 'categorie']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'categorie')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'created_on', 'approved')
    search_fields = ['name', 'email', 'post']
    list_filter = ('approved', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Scam)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'email', 'media', 'created_on', 'approved')
    search_fields = ['name', 'email', 'media']
    list_filter = ('approved', 'email', 'media')
    actions = ['approve_scams']

    def approve_scams(self, request, queryset):
        queryset.update(approved=True)
