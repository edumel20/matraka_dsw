from django.contrib import admin

from .models import Post, PostLabelingDetail


class PostLabelDetailInline(admin.TabularInline):
    model = PostLabelingDetail
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'slug')
