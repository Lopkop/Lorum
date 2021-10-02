from django.urls import path

from .views import (article_view,
                    forum_page_view,
                    programming_page_view,
                    electronics_page_view,
                    mathematics_page_view,
                    physics_page_view,
                    other_page_view,
                    security_page_view,
                    )

urlpatterns = [
    path('', forum_page_view, name='forums'),

    path('programming/<int:pk>', article_view, name='programming_article'),
    path('electronics/<int:pk>', article_view, name='electronics_article'),
    path('security/<int:pk>', article_view, name='security_article'),
    path('other/<int:pk>', article_view, name='other_article'),
    path('mathematics/<int:pk>', article_view, name='math_article'),
    path('physics/<int:pk>', article_view, name='physics_article'),

    path('programming/', programming_page_view, name='programming'),
    path('electronics/', electronics_page_view, name='electronics'),
    path('security/', security_page_view, name='security'),
    path('other/', other_page_view, name='other'),
    path('mathematics/', mathematics_page_view, name='mathematics'),
    path('physics/', physics_page_view, name='physics'),
]
