from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.product_view),
    path("products/<int:id>/", views.product_detail),
]
