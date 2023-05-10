from rest_framework import serializers
from inmuebleslist_app.models import Comentario, Empresa, Edificacion


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"


class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Edificacion
        fields = "__all__"


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    edificacionlist = EdificacionSerializer(
        many=True, read_only=True
    )  ## show all items with full data
    # edificacionlist = serializers.StringRelatedField(many=True) ## show all items with str data
    # edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) ## show all items with id
    # edificacionlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="edificacion-detalle"
    # )  ## show all items with endpoint

    class Meta:
        model = Empresa
        fields = "__all__"
