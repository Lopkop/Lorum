from django.urls import path

from .views import ForumPageView, article_view

urlpatterns = [
    path('', ForumPageView.as_view(), name='forum'),
    path('<int:pk>', article_view, name='article'),
]
