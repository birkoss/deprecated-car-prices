from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cars import models as api_models

from . import serializers as api_serializers


class MakeViewSet(viewsets.ModelViewSet):
    """
    Makes list
    """
    queryset = api_models.Make.objects.all()
    serializer_class = api_serializers.MakeSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'], name='Models')
    def models(self, request, pk):
        """
        All models from this brands
        """
        models = api_models.Model.objects.filter(make__pk=pk)
        serializer = api_serializers.ModelSerializer(
            instance=models,
            many=True
        )
        return Response(serializer.data)


class PaymentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Payment Types list
    """
    queryset = api_models.PaymentType.objects.all()
    serializer_class = api_serializers.PaymentTypeSerializer
    permission_classes = [IsAuthenticated]
