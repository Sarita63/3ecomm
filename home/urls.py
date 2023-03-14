from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('subcat/<slug>', SubcategoryView.as_view(),name='subcat'),
    path('detail/<slug>', DetailView.as_view(),name='detail'),
    path('search/',SearchView.as_view(),name='search'),
    path('register/',signup,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('cart/<slug>',cart,name='cart'),
    path('my_cart/',CartView.as_view(),name='my_cart'),
    path('delete_cart/<slug>',delete_cart,name='delete_cart'),
    path('reduce_cart/<slug>',reduce_cart,name='reduce_cart'),
    
  ]
