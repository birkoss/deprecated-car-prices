from rest_framework import serializers

from cars import models as api_models


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Make
        fields = ('id', 'name', 'slug')


class ModelReadSerializer(serializers.ModelSerializer):
    make = MakeSerializer()

    class Meta:
        model = api_models.Model
        fields = ('id', 'name', 'slug', 'year', 'make')


class ModelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Model
        fields = ('name', 'year')


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.PaymentType
        fields = ('id', 'name', 'slug')


class TrimReadSerializer(serializers.ModelSerializer):
    model = ModelReadSerializer()

    class Meta:
        model = api_models.Trim
        fields = ('id', 'name', 'slug', 'nice_name', 'model')


class TrimWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Trim
        fields = ('name', 'nice_name')
