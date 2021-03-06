from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

js_info_dict = {
    'packages': (
        'django.conf',
        'mainpage.wlansi',
    ),
}

urlpatterns = patterns('',
    url(r'^admin/cms/plugin/markup/', include('cmsplugin_markup.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/js/$', 'django.views.i18n.javascript_catalog', js_info_dict),

    url(r'^paypal/ipn/$', 'mainpage.wlansi.buynow.views.ipn', name='paypal-ipn'),
    url(r'^paypal/order/$', 'mainpage.wlansi.buynow.views.pdt', name='paypal-order'),
    url(r'^paypal/button/$', 'mainpage.wlansi.buynow.views.paypal_button', name='paypal-button'),

    url(r'^paypal/donation/$', 'mainpage.wlansi.buynow.views.pdt', {'template': 'donations/pdt.html'}, name='paypal-donation'),

    url(r'^', include('filer.server.urls')),

    url(r'^', include('cms.urls')),
)

# For development, serve static files through Django
if getattr(settings, 'DEBUG', False):
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
