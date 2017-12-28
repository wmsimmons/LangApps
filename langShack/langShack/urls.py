from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import langShack.views
import contact.views

admin.autodiscover()

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', langShack.views.home),
    url(r'^ourmission', langShack.views.ourMission),
    url(r'^langblog/', include('langBlog.urls')),
    url(r'^contact/$', contact.views.contactUs, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]