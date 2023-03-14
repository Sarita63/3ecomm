
from django.urls import path, include
from .views import ItemViewSet,ItemFilterViewSet,CRUDItemViewSet
from rest_framework import routers, serializers, viewsets



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('item_filter/',ItemFilterViewSet.as_view(),name='item_filter'),
    path('crud_item/<int:pk>',CRUDItemViewSet.as_view(),name='crud_item')
    
    
]