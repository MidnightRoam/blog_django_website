from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from .models import Post


class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "blog_website/index.html", {"page_obj": page_obj})


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog_website/about.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog_website/contact.html")


class BlogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog_website/blog_page.html")


class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog_website/thanks.html")
