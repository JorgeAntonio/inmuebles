from inmuebleslist_app.api.serializers import EmpresaSerializer, EdificacionSerializer
from inmuebleslist_app.models import Empresa, Edificacion
from rest_framework.response import Response

# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class EmpresaApiview(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(
            empresas, many=True, context={"request": request}
        )  ## add context to get all items with endpoints
        return Response(serializer.data)

    def post(selt, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetalleApiview(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response(
                {"Error": "Empresa not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = EmpresaSerializer(empresa, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response(
                {"Error": "Empresa not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = EmpresaSerializer(
            empresa, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response(
                {"Error": "Empresa not found"}, status=status.HTTP_404_NOT_FOUND
            )
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EdificacionApiview(APIView):
    def get(self, request):
        inmuebles = Edificacion.objects.all()
        serializer = EdificacionSerializer(inmuebles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EdificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdificacionDetailApiView(APIView):
    def get(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(
                {"Error": "Inmueble does not exists"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = EdificacionSerializer(inmueble)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(
                {"Error": "Inmueble does not exists"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = EdificacionSerializer(inmueble, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(
                {"Error": "Inmueble does not exists"}, status=status.HTTP_404_NOT_FOUND
            )
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
