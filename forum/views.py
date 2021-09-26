from django.views import generic

from forum.models import Article


class ForumPageView(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'forum/home.html'


class ArticleView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'forum/article.html'


