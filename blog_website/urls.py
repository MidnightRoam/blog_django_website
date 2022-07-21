from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import HomeView, AboutView, PostDetailView, ThanksView, RegisterView, LoginView, SuccessView, FeedBackView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('post/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('thanks/', ThanksView.as_view(), name='thanks_page'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('contact/success/', SuccessView.as_view(), name='success'),
]
