from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
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

    @action(detail=True, methods=['GET', 'POST'], name='Models')
    def models(self, request, pk):
        """
        All models from this brands
        """
        make = None
        try:
            make = api_models.Make.objects.get(pk=pk)
        except api_models.Make.DoesNotExist:
            raise NotFound()

        if make is None:
            raise NotFound()

        if request.method == 'POST':
            serializer = api_serializers.ModelWriteSerializer(
                data=request.data
            )
            serializer.is_valid(raise_exception=True)

            model = serializer.save(make=make)

            data = api_serializers.ModelReadSerializer(model).data

            return Response(data)

        if request.method == 'GET':
            models = api_models.Model.objects.filter(make__pk=pk)
            serializer = api_serializers.ModelReadSerializer(
                instance=models,
                many=True
            )
            return Response(serializer.data)


class ModelViewSet(viewsets.ModelViewSet):
    """
    Models list
    """
    queryset = api_models.Model.objects.all()
    serializer_class = api_serializers.ModelReadSerializer
    permission_classes = [IsAuthenticated]


class PaymentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Payment Types list
    """
    queryset = api_models.PaymentType.objects.all()
    serializer_class = api_serializers.PaymentTypeSerializer
    permission_classes = [IsAuthenticated]
