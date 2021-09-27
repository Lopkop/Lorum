from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from forum.models import Article, Comment
from .forms import CommentForm


class ForumPageView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'forum/home.html'


def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if isinstance(request.user, AnonymousUser):
            return HttpResponse("<h2 id='id-error'>Sorry, but you can't comment any post in security concerns, "
                                "because you are not logged in.</h2>")
        Comment.objects.create(user=request.user, article=article, body=request.POST.get('body'))
    return render(request, 'forum/article.html', {'article': article, 'comment_form': CommentForm,
                                                  'comments': Comment.objects.filter(article=article)})
