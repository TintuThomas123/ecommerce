from django.urls import path
from .import views
from ecommerceproject import settings
# from django.conf import settings
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
     path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail')
]