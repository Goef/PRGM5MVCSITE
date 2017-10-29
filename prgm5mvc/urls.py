from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from prgm5mvc.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^story1$', core_views.home, {'template_name': 'story1.html'},name='story1'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
]
