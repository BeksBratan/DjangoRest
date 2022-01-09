from django.contrib import admin
from django.urls import path
from MovieBackend import views as movieviews
from ShopBackend import views as shopviews


urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/v1/data/', movieviews.index),
    path('api/v1/movies/', movieviews.movie_list_view),
    path('api/v1/movies/<int:id>/', movieviews.movie_detail_view),

    path('api/v1/products/', shopviews.Product_list_view),
    path('api/v1/products/<int:id>/', shopviews.Product_detail_view),

]