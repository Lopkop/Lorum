from django.urls import path

from .views import ForumPageView

urlpatterns = [
    path('', ForumPageView.as_view(), name='forum'),
]
