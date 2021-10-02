from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render

from .models import Article
from .forms import CommentForm
from .services import create_comment, get_article, create_or_delete_like
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
