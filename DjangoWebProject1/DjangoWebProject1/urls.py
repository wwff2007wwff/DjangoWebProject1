"""
DjangoWebProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path
from django.conf.urls import include, url
import MyApp1.views
import myAPP2.views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    url(r'^$', MyApp1.views.index, name='index1'),
    url(r'^home$', MyApp1.views.index, name='home2'),
    url(r'^home3/hom$', myAPP2.views.index, name='index3'),
    url(r'^home2$', myAPP2.views.index, name='home4'),
]
