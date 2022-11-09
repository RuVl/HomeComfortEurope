from django.urls import path

from mainapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('search-result/', search_result, name='search_result'),
    path('become-a-stocklist/', become_a_stocklist, name='become_a_stocklist'),
    path('news/', news, name='news'),
    path('news/<slug:concrete>/', concrete_news, name='concrete_news'),
    path('our-story/', about_us, name='about_us'),
    path('ethos/', ethos, name='ethos'),
    path('design-studio/', design_studio, name='design_studio'),
    path('fulfilment/', fulfilment, name='fulfilment'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('cookies/', cookies, name='cookies'),
    path('product/<int:pk>', get_product, name='product')

]
