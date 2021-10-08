from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import exceptions

from .models import Article
from .forms import CommentForm, ArticleForm
from .services import create_comment, get_article, create_or_delete_like, edit_article
from .configs import categories


def forum_page_view(request):
    return render(request, 'forum/home.html', {'articles': Article.objects.all(),
                                               '1_categories': categories[::2],
                                               '2_categories': categories[1::2],
                                               })


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
                                                  'comments': article.get_comments(article),
                                                  'count_of_comments': article.get_comments(article).count(),
                                                  'likes': article.get_likes(article).count(),
                                                  })


@login_required(login_url='/accounts/login/')
def my_articles_view(request):
    return render(request, 'forum/my_articles.html', {'articles': Article.objects.filter(user=request.user)})


@login_required(login_url='/accounts/login/')
def create_article(request):
    if request.method == 'POST':
        Article.objects.create(user=request.user, title=request.POST.get('title'), body=request.POST.get('body'),
                               category=request.POST.get('category'))
        return redirect('/forums/my-articles')
    return render(request, 'forum/add_article.html', {'form': ArticleForm})


@login_required(login_url='/accounts/login/')
def edit_article_view(request, pk):
    if request.user == (article := get_article(pk)).user:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                edit_article(article, form.cleaned_data)
                return HttpResponseRedirect(reverse('my_articles'))
        return render(request, 'forum/edit_article.html',
                      {'form': ArticleForm({'title': article, 'category': article.category,
                                            'body': article.body})})
    raise exceptions.PermissionDenied()


@login_required(login_url='/accounts/login/')
def delete_article_view(request, pk):
    try:
        Article.objects.filter(user=request.user, pk=get_article(pk).pk).delete()
    except exceptions.ObjectDoesNotExist:
        return HttpResponse('Article does not exist')
    return redirect('/forums/my-articles/')


def programming_page_view(request):
    return render(request, 'forum/programming.html', {'articles': Article.objects.filter(category='programming')})


def security_page_view(request):
    return render(request, 'forum/security.html', {'articles': Article.objects.filter(category='cyber security')})


def mathematics_page_view(request):
    return render(request, 'forum/mathematics.html', {'articles': Article.objects.filter(category='mathematics')})


def physics_page_view(request):
    return render(request, 'forum/physics.html', {'articles': Article.objects.filter(category='physics')})


def electronics_page_view(request):
    return render(request, 'forum/electronics.html', {'articles': Article.objects.filter(category='electronics')})


def other_page_view(request):
    return render(request, 'forum/other.html', {'articles': Article.objects.filter(category='other')})
