# from .models import Inmmueble
# from django.http import JsonResponse
#
# # Create your views here.
#
#
# def inmueble_list(request):
#     inmuebles = Inmmueble.objects.all()
#     data = {
#         'inmuebles': list(inmuebles.values())
#     }
#     return JsonResponse(data)
#
#
# def inmueble_detalle(request, pk):
#     inmueble = Inmmueble.objects.get(pk=pk)
#     data = {
#         'direccion': inmueble.direccion,
#         'pais': inmueble.pais,
#         'imagen': inmueble.imagen,
#         'active': inmueble.active,
#         'descripcion': inmueble.descripcion
#     }
#
#     return JsonResponse(data)
