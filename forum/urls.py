from django.urls import path

from .views import ForumPageView, ArticleView

urlpatterns = [
    path('', ForumPageView.as_view(), name='forum'),
    path('<int:pk>', ArticleView.as_view(), name='article'),
]
