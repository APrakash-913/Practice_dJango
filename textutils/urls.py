"""textutils URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index1, name='index1'),
    path('about', views.about, name='about'), 
    # path(str jo bataayega ki website ke URL ke baad kya append hona chahiye, konsa fn run hona chahiye, koi aacha se name dede)
#---------------------------------------------------------------------------------------------------------------------------------#   
    # creating Pipeline.
    
    path('index', views.index, name="index"),
    path('removepunc', views.removepunc, name="rempun"),
    path('capitalisefirst', views.capfirst, name="capfirst"), 
    path('charremove', views.charremove, name="charremove"), 
    path('spaceremove', views.spaceremove, name="spaceremove"), 
    path('newlineremove', views.newlineremove, name="capfirsnewlineremove"), 
    path('analyze', views.analyze, name="analyze")

]
