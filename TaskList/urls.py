from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from TaskLists.views import HomePageView
from TaskLists.views import home, done, logout, error, form, form2, close_login_popup, user, newIdea
from TaskLists.facebook import facebook_view

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TaskList.views.home', name='home'),
    # url(r'^TaskList/', include('TaskList.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r"^$", TemplateView.as_view(template_name="index.html"))
    #url(r'^$', HomePageView.as_view()),
    #added
    url(r'^$', home, name='home'),
    url(r'^user/$', user, name='user'),
    #url(r'^newidea/$', newIdea, name='newidea'),
    url(r'^newidea/$', newIdea, name='newidea'),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^form/$', form, name='form'),
    url(r'^form2/$', form2, name='form2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fb/', facebook_view, name='fb_app'),
    url(r'^close_login_popup/$', close_login_popup, name='login_popup_close'),
    url(r'', include('social_auth.urls')),
)

urlpatterns += staticfiles_urlpatterns()
