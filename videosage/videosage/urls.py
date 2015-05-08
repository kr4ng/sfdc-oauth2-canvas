from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'videosage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home', 'webapp.views.home', name='home'),
    url(r'^auth/salesforce/callback/', 'webapp.views.redirecturl', name='redirect')
)
