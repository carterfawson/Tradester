from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Tradester.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'mvp.views.home', name='mvphome'),
    url(r'^admin/', include(admin.site.urls)),
]
