from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dumacodechallenge.views.home', name='home'),
    # url(r'^dumacodechallenge/', include('dumacodechallenge.foo.urls')),

    (r'^', include('locations.urls')),
)
