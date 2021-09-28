from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from forum.models import Article, Like
from .forms import CommentForm
from .services import create_comment, get_article, get_article_comments, create_or_delete_like, get_article_likes


class ForumPageView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'forum/home.html'


def article_view(request, pk):
    article = get_article(pk)
    if request.method == 'POST':
        if isinstance(request.user, AnonymousUser):
            return HttpResponse("<h2 id='id-error'>Sorry, but you can't comment or like any post in security concerns, "
                                "because you are not logged in.</h2>")
        elif request.POST.get('body'):
            create_comment(request.user, article, request.POST.get('body'))
        else:
            create_or_delete_like(request.user, article)

    return render(request, 'forum/article.html', {'article': article, 'comment_form': CommentForm,
                                                  'comments': get_article_comments(article),
                                                  'count_of_comments': get_article_comments(article).count(),
                                                  'likes': get_article_likes(article).count()})
