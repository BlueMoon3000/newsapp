from django.conf.urls import patterns, include, url

from django.contrib import admin

from core.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),


)
