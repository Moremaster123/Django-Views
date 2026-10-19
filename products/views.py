from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import ProductModel

CAMPOS = ["title", "price", "description", "seller", "color", "product_dimensions"]


class ProductListView(ListView):
    model = ProductModel
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = ProductModel
    template_name = "products/product_form.html"
    fields = CAMPOS


class ProductUpdateView(UpdateView):
    model = ProductModel
    template_name = "products/product_form.html"
    fields = CAMPOS


class ProductDeleteView(DeleteView):
    model = ProductModel
    template_name = "products/product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("product-list")
