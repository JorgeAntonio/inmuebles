from inmuebleslist_app.api.serializers import InmuebleSerializer
from inmuebleslist_app.models import Inmmueble
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# @api_view(['GET', 'POST'])
# def inmueble_list(request):
#     if request.method == 'GET':
#         try:
#             inmuebles = Inmmueble.objects.all()
#             serializer = InmuebleSerializer(inmuebles, many=True)
#             return Response(serializer.data)
#         except Inmmueble.DoesNotExist:
#             return Response({"Inmueble does not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'POST':
#         deserializer = InmuebleSerializer(data=request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data)
#         else:
#             return Response(deserializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def inmueble_detalle(request, pk):
#     if request.method == 'GET':
#         try:
#             inmueble = Inmmueble.objects.get(pk=pk)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmmueble.DoesNotExist:
#             return Response({'Error': 'Inmueble does not exists'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         inmueble = Inmmueble.objects.get(pk=pk)
#         deserializer = InmuebleSerializer(inmueble, data=request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data)
#         else:
#             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmmueble.objects.get(pk=pk)
#             inmueble.delete()
#         except Inmmueble.DoesNotExist:
#             return Response({'Error': 'Inmueble does not exists'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_204_NO_CONTENT)

class InmuebleListApiview(APIView):
    @staticmethod
    def get(request):
        inmuebles = Inmmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = InmuebleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InmuebleDetailApiView(APIView):
    @staticmethod
    def get(request, pk):
        try:
            inmueble = Inmmueble.objects.get(pk=pk)
        except Inmmueble.DoesNotExist:
            return Response({'Error': 'Inmueble does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, pk):
        try:
            inmueble = Inmmueble.objects.get(pk=pk)
        except Inmmueble.DoesNotExist:
            return Response({'Error': 'Inmueble does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InmuebleSerializer(inmueble, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        try:
            inmueble = Inmmueble.objects.get(pk=pk)
        except Inmmueble.DoesNotExist:
            return Response({'Error': 'Inmueble does not exists'}, status=status.HTTP_404_NOT_FOUND)
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
