"""cryptotracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from cryptos.views import home, CriptosList, Portfolio, AlgorithPortfolio, ProfitPortfolio
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from cryptos.views import *
from codes.views import CodeList


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/auth/', include(('auth.urls','auth'))),
    url(r'^criptos', CriptosList.as_view()),#insert
    path('my-cripto/<int:pk>/', CriptosList.as_view()),
    path('portfolio/', Portfolio.as_view()),#just get
    path('code/', CodeList.as_view()),
    path('invested/', AlgorithPortfolio.as_view()),
    path('profit/', ProfitPortfolio.as_view())

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
