"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from shop_psb import views as accounts_views

urlpatterns = [
    url(r'^$', accounts_views.IndexView.as_view(), name='root'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^shop_psb/signup$', accounts_views.CreateUserView.as_view(), name="signup"),                # 회원가입 화면
    url(r'^shop_psb/signup/done$', accounts_views.RegisteredView.as_view(), name="create_user_done"), # 회원가입이 완료된 화면
]