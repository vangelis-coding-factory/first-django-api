from django.urls import path
#from .views import ProductDetailView, ProductListView
from .views import product_list, product_detail

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>", product_detail, name="product-detail"),
]

""" urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
] """