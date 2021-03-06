"""demoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.http.response import HttpResponse

from demoweb.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    # path('bookmark/', None, name="bookmark-index")
    path('bookmark/', include('bookmark.urls')),    # bookmark로 시작되는 url 설정 관리는 bookmark/urls.py 에서 처리합니다.
    path('blog/', include('blog.urls')),            # blog로 시작되는 url 설정 관리는 blog/urls.py 에서 처리합니다.
]
