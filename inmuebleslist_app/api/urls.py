from django.urls import path

from inmuebleslist_app.api.views import (
    EmpresaApiview,
    EdificacionApiview,
    EdificacionDetailApiView,
    EmpresaDetalleApiview,
)


urlpatterns = [
    path("list/", EdificacionApiview.as_view(), name="edificacion"),
    path("<int:pk>/", EdificacionDetailApiView.as_view(), name="edificacion-detail"),
    path("empresa/", EmpresaApiview.as_view(), name="empresa"),
    path("empresa/<int:pk>/", EmpresaDetalleApiview.as_view(), name="empresa-detail"),
]
