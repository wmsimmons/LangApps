from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import langShack.views
import contact.views
import papahana.views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', langShack.views.home),
    url(r'^ourmission', langShack.views.ourMission),
    url(r'^langblog/', include('langBlog.urls')),
    url(r'^contact/$', contact.views.contactUs, name='contact'),
    url(r'^workbench-start/$', papahana.views.workbench_start),
    url(r'^workbench/$', papahana.views.workbench),
    url(r'^upload/', papahana.views.simple_upload),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)