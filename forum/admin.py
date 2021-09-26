from django.contrib import admin

from forum.models import Article, Comment, Like


class CommentInline(admin.TabularInline):
    extra = 0
    model = Comment


class LikeInline(admin.TabularInline):
    extra = 0
    model = Like


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        LikeInline
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Like)
