from django.contrib.auth.models import User
from django.db import models

from .configs import categories


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='account deleted')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30, choices=categories)

    def get_comments(self, article):
        return Comment.objects.filter(article=article)

    def get_likes(self, article):
        return Like.objects.filter(article=article)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return str(self.count)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
