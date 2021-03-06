from django.conf.urls import patterns, url, include
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'saleor.views.home', name='home'),
    url(r'^products/', include('product.urls', namespace='product')),
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'^checkout/', include('checkout.urls', namespace='checkout')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^account/', include('registration.urls', namespace='registration')),
    url(r'^profile/', include('userprofile.urls', namespace='profile')),
    url(r'^', include('payments.urls')),
)
