from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^testsplash/', include('testproject2.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
