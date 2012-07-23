from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^new/video$', 'video.views.new_video'),
    url(r'^get/video/(?P<video_id>.+)$', 'video.views.get_video'),
    # Examples:
    # url(r'^$', 'phocas.views.home', name='home'),
    # url(r'^phocas/', include('phocas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
