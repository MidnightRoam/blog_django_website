from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog_website/index.html")


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
