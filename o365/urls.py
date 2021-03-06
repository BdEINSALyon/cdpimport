"""import URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from o365 import views

app_name = 'o365'
urlpatterns = [
    url(r'^teams$', views.TeamsView.as_view(), name='teams'),
    url(r'^team/(?P<gid>[-\w]+)$', views.TeamView.as_view(), name='team'),
    url(r'^team/(?P<gid>[-\w]+)/clear$', views.ClearTeamView.as_view(), name='team_clear'),
    url(r'^team/(?P<gid>[-\w]+)/register$', views.RegisterMembersTeamView.as_view(), name='team_register'),
]
