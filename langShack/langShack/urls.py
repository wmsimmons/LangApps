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
    url(r'^admin/', admin.site.urls),
    url(r'^langblog/', include('langBlog.urls')),
    url(r'^contact/$', contact.views.contactUs, name='contact'),
    # url(r'^workbench-start/$', papahana.views.workbench_start),
    # url(r'^workbench/$', papahana.views.workbench),
    # url(r'^upload/', papahana.views.simple_upload),
    url(r'^api-auth/', include('rest_framework.urls'))
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)


from django.conf.urls import url, include
from rest_framework import routers
from papahana import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
