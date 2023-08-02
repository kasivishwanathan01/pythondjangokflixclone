
"""
URL configuration for Protfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Mypro import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('browse', views.browse, name='browse'),
    path('latest', views.latest, name='latest'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('movies', views.movies, name='movies'),
    path('mylist', views.mylist, name='mylist'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
    path('single', views.single, name='single'),
    path('tvshow', views.tvshow, name='tvshow'),

    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),
]
