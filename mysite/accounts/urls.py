from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"
urlpatterns = [
    url(r'^entrar/$', auth_views.login, {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^cadastro/$', views.register, name="register"),
    url(r'^sair/$', auth_views.logout, {'next_page': 'blog:post_list'}, name="logout"),
]
