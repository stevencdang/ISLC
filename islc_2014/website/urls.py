from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',
        'website.views.home', name='index'),
    url(r'^about',
        'website.views.home', name='index'),
    url(r'^proposals',
        'website.views.proposal', name='proposal'),
    url(r'^registration',
        'website.views.registration', name='registration'),
    url(r'^schedule',
        'website.views.schedule', name='schedule'),
    url(r'^participants',
        'website.views.participants', name='participants'),
    url(r'^travel',
        'website.views.travel', name='travel'),
    url(r'^slc-information',
        'website.views.slc_info', name='slc_information'),
    url(r'^planning-committee',
        'website.views.planning', name='planning_committee'),
    url(r'^alumni-panel',
        'website.views.alumni_panel', name='alumni_panel'),
)
