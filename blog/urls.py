from django.urls import path
from .views import hello, BlogListView
urlpatterns = [
    path('hello/', hello),
    path('blog/', BlogListView.as_view())
]