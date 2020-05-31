from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cars import models as api_models

from . import serializers as api_serializers


class NoCreateViewSet(viewsets.ModelViewSet):
    """
    Disable the Create method (POST) and
    show a specific message
    """
    response_no_create = "This method is NOT available"

    def create(self, request):
        response = {
            'detail': self.response_no_create
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class NoPartialUpdateViewSet(viewsets.ModelViewSet):
    """
    Disable the Partial Update method (PATCH) and
    show a specific message
    """
    response_no_partial_update = "This method is NOT available. Use PUT instead"

    def partial_update(self, request, pk):
        response = {
            'detail': self.response_no_partial_update
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UpdateReadWriteViewSet(viewsets.ModelViewSet):
    """
    Used to allow update using a specific Write Serializer and 
    return the instance using a specific Read Serializer
    """
    read_serializer_class = None
    write_serializer_class = None

    def update(self, request, *args, **kwargs):
        """
        Update using a WriteSerializer and return a ReadSerializer
        """
        instance = self.get_object()

        serializer = self.write_serializer_class(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(self.read_serializer_class(instance).data)


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


class ModelViewSet(NoCreateViewSet, NoPartialUpdateViewSet, UpdateReadWriteViewSet, viewsets.ModelViewSet):
    """
    Models list
    """
    queryset = api_models.Model.objects.all()
    serializer_class = api_serializers.ModelReadSerializer
    permission_classes = [IsAuthenticated]

    response_no_create = 'Use /api/makes/{id}/models/ to create a model'
    response_no_partial_update = 'Use PUT to edit a model'

    read_serializer_class = serializer_class
    write_serializer_class = api_serializers.ModelWriteSerializer

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


class PaymentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Payment Types list
    """
    queryset = api_models.PaymentType.objects.all()
    serializer_class = api_serializers.PaymentTypeSerializer
    permission_classes = [IsAuthenticated]


class TrimViewSet(NoCreateViewSet, NoPartialUpdateViewSet, UpdateReadWriteViewSet, viewsets.ModelViewSet):
    """
    Trims list
    """
    queryset = api_models.Trim.objects.all()
    serializer_class = api_serializers.TrimReadSerializer
    permission_classes = [IsAuthenticated]

    response_no_create = 'Use /api/models/{id}/trims/ to create a trim'
    response_no_partial_update = 'Use PUT to edit a trim'

    read_serializer_class = serializer_class
    write_serializer_class = api_serializers.ModelWriteSerializer
