from django.conf.urls import patterns, include, url
from bow.views import my_view_that_updates_plist,ResListView,RegisterView
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rating_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rate/(?P<name>\w*[-]\d+)/$', ResListView.as_view()),
    url(r'^plist_exp/(?P<name>\w*[-]\d+)/$',my_view_that_updates_plist),
    url(r'^login/$', RegisterView.as_view()),
    url(r'^index/$',TemplateView.as_view(template_name='index.html'))
)
