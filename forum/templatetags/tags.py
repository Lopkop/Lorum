from django import template

register = template.Library()


@register.simple_tag
def get_comments_count(article):
    return article.get_comments(article).count()


@register.simple_tag
def get_likes_count(article):
    return article.get_likes(article).count()
