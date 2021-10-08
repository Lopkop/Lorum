from django.urls import path

from .views import SignUpView, user_page_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>', user_page_view, name='user_page'),
]
