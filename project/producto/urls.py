from django.urls import include, path
from .views import index

app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    #path("producto/", include("producto.urls", "producto")),
]
