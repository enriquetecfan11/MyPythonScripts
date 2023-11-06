from django.urls import path
from .views import *

urlpatterns = [
    path('brands/', BrandListView.as_view(), name='brands'),
    path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:id>/', BrandRetrieveView.as_view(), name='brand'),
    path('brands/<int:id>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:id>/delete/', BrandDestroyView.as_view(), name='brand_delete'),
]