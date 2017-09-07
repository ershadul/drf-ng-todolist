from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib.auth import views as auth_views

from . import views

todo_router = routers.DefaultRouter()
todo_router.register(r'todos', views.TodoViewSet, base_name='todos')


urlpatterns = [
    # Send base.html to angular
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.index, name='index'),
    url('^api/', include(todo_router.urls)),
]
