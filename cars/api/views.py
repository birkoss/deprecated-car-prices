from rest_framework import mixins, status, viewsets
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

    def create(self, request):
        response = {
            'detail': 'Use /api/makes/{id}/models/ to create a model'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        response = {
            'detail': 'Use PUT to edit a model'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(self.serializer_class(instance).data)

    @action(detail=True, methods=['GET', 'POST'], name='Trims')
    def trims(self, request, pk):
        """
        All models from this brands
        """
        model = None
        try:
            model = api_models.Model.objects.get(pk=pk)
        except api_models.Model.DoesNotExist:
            raise NotFound()

        if model is None:
            raise NotFound()

        if request.method == 'POST':
            serializer = api_serializers.TrimWriteSerializer(
                data=request.data
            )
            serializer.is_valid(raise_exception=True)

            trim = serializer.save(model=model)

            data = api_serializers.TrimReadSerializer(trim).data

            return Response(data)

        if request.method == 'GET':
            print("GET...")
            trims = api_models.Trim.objects.filter(model=model)
            serializer = api_serializers.TrimReadSerializer(
                instance=trims,
                many=True
            )
            return Response(serializer.data)


    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return api_serializers.ModelWriteSerializer
        return self.serializer_class


class PaymentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Payment Types list
    """
    queryset = api_models.PaymentType.objects.all()
    serializer_class = api_serializers.PaymentTypeSerializer
    permission_classes = [IsAuthenticated]
