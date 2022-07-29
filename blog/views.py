from django.shortcuts import render
from django.views import View


def hello(request):
    print('Hello')
    return render(request, 'blog/hello.html')


class BlogListView(View):
    def get(self, request):
        return render(request, 'blog/bloglist.html')


class IndexView(View):
    def get(self, request):
        return render(request, 'blog/index.html')



