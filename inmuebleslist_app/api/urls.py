from django.urls import path

from inmuebleslist_app.api.views import (
    EmpresaApiview,
    EdificacionApiview,
    EdificacionDetailApiView,
    EmpresaDetalleApiview,
    ComentarioList,
    ComentarioDetail,
)


urlpatterns = [
    path("edificacion/", EdificacionApiview.as_view(), name="edificacion"),
    path(
        "edificacion/<int:pk>/",
        EdificacionDetailApiView.as_view(),
        name="edificacion-detail",
    ),
    path("empresa/", EmpresaApiview.as_view(), name="empresa"),
    path("empresa/<int:pk>/", EmpresaDetalleApiview.as_view(), name="empresa-detail"),
    path(
        "edificacion/<int:pk>/comentario/",
        EdificacionDetailApiView.as_view(),
        name="comentario-list",
    ),
    path(
        "edificacion/comentario/<int:pk>/",
        ComentarioDetail.as_view(),
        name="comentario-detail",
    ),
]
