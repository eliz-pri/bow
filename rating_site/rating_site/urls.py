from django.conf.urls import patterns, include, url
from bow.views import my_view_that_updates_plist,ResListView,login_user
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rating_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', ResListView.as_view()),
    url(r'^plist_exp/$',my_view_that_updates_plist),
    url(r'^login/$', login_user),
)
