from forum.models import Comment, Article, Like


def create_comment(user, article, text):
    Comment.objects.create(user=user, article=article, body=text).save()


def create_article(user, title, body, category=None):
    if category:
        Article.objects.create(user=user, title=title, body=body, category=category).save()
    else:
        Article.objects.create(user=user, title=title, body=body).save()


def create_or_delete_like(user, article):
    new_like, created = Like.objects.get_or_create(user=user, article=article, count=1)
    if not created:
        Like.objects.filter(user=user, article=article).delete()


def get_article(pk):
    return Article.objects.get(pk=pk)


def edit_article(article, data):
    article.title = data['title']
    article.category = data['category']
    article.body = data['body']
    article.save()
