from django.urls import path
from .views import hello, BlogListView, IndexView
urlpatterns = [
    path('hello/', hello),
    path('blog/', BlogListView.as_view()),
    path('', IndexView.as_view())
]