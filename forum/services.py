from forum.models import Comment, Article


def create_comment(user, article, text):
    Comment.objects.create(user=user, article=article, body=text).save()


def create_article(user, title, body):
    Article.objects.create(user=user, title=title, body=body).save()


def get_article(pk):
    return Article.objects.get(pk=pk)


def get_article_comments(article):
    return Comment.objects.filter(article=article)
