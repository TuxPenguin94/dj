from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'loesk_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), #grappelli URL
    url(r'^admin/', include(admin.site.urls)), # admin URL
    url(r'^basicview/', include('call.urls')),
    url(r'^attachments/', include('attachments.urls', namespace='attachments')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('call.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
