from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from taggit.models import Tag

from .models import Post, Comment
from .forms import RegisterForm, LoginForm, FeedBackForm, CommentForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "blog_website/index.html", {"page_obj": page_obj})


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog_website/about.html")


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        common_tags = Post.tag.most_common()
        last_posts = Post.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, "blog_website/post_detail.html", {"post": post,
                                                                 "common_tags": common_tags,
                                                                 "last_posts": last_posts,
                                                                 "comment_form": comment_form})

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, url=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, "blog_website/post_detail.html", {"comment_form": comment_form})


class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "blog_website/thanks.html")


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'blog_website/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'blog_website/signup.html', {'form': form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "blog_website/signin.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, "blog_website/signin.html", {"form": form})


class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, "blog_website/contact.html", {'form': form,
                                                             'title': 'Contact with me'
                                                             })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'From {name} | {subject}', message, from_email, ['midnightroam1@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header')
            return HttpResponseRedirect('success')
        return render(request, "blog_website/contact.html", {"form": form})


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog_website/thanks.html', {'title': 'Thanks'})


class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = Post.objects.filter(
                Q(h1__icontains=query) | Q(content__icontains=query)
            )
        paginator = Paginator(results, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog_website/search.html', {'title': 'Search',
                                                            'results': page_obj,
                                                            'count': paginator.count
                                                            })


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tag=tag)
        common_tags = Post.tag.most_common()
        return render(request, 'blog_website/tag.html', {"posts": posts,
                                                        "title": f'#{tag}',
                                                        "common_tags": common_tags
                                                        })

