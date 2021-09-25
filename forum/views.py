from django.views.generic import TemplateView


class ForumPageView(TemplateView):
    template_name = 'forum/home.html'
