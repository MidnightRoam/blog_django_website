from django.urls import path

from .views import HomeView, AboutView, ContactView, BlogView, ThanksView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog_page/', BlogView.as_view(), name='blog_page'),
    path('thanks/', ThanksView.as_view(), name='thanks_page'),
]
