from registration.backends.simple.views import RegistrationView
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from rango import views
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    #url(r'^accounts/password/change/$', MyRegistrationView.as_view(), name='change_password'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)



#urlpatterns = patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^rango/', include('rango.urls')),
#    url(r'^accounts/', include('registration.backends.simple.urls')),
#)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )



