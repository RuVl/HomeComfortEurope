from django.conf.urls.static import static
from django.urls import path

from HomeComfortEurope import settings
from mainapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('search-result/', search_result, name='search_result'),
    path('news/', news, name='news'),
    path('news/<slug:concrete>/', concrete_news, name='concrete_news'),
    path('our-story/', about_us, name='about_us'),
    path('ethos/', ethos, name='ethos'),
    path('design-studio/', design_studio, name='design_studio'),
    path('fulfilment/', fulfilment, name='fulfilment'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('cookies/', cookies, name='cookies'),
    path('product/<int:pk>', get_product, name='product'),
    path('type/<int:pk>', get_products_sorted_by_type, name='type'),
    path('collection/<int:pk>', get_types_sorted_by_collections, name='collection')
    # path('types/' )
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
