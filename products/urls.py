from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("crear/", views.ProductCreateView.as_view(), name="product-create"),
    path("<int:pk>/editar/", views.ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/eliminar/", views.ProductDeleteView.as_view(), name="product-delete"),
]
