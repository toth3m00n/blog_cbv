from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from mptt.admin import DraggableMPTTAdmin
from .models import Category, Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdminPage(DjangoMpttAdmin):
    """
    Админ-панель модели комментариев
    """
    pass
