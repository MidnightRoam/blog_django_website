from django.urls import path

from .views import HomeView, AboutView, ContactView, PostDetailView, ThanksView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('thanks/', ThanksView.as_view(), name='thanks_page'),
]
