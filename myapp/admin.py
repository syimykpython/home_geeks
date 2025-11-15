from django.contrib import admin
from .models import Post, Category, Tag, Comment




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'category', 'rate', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags')
    filter_horizontal = ('tags',)





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
