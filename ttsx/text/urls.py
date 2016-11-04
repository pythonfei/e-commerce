from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^list([0-9]*)/$',views.list,name ='list'),
    url(r'^detail(?P<id>[0-9]+)/$',views.detail,name ='detail'),
    # url(r'detail/$',views.detail,name = 'detail'),
    url(r'^base/$',views.base,name='base'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^place_order/$',views.place_order,name='place_order'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^success/$',views.success,name='success'),
]
