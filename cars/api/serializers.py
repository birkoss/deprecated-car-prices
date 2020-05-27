from rest_framework import serializers

from cars import models as api_models


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Make
        fields = ('id', 'name', 'slug')


class ModelSerializer(serializers.ModelSerializer):
    make = MakeSerializer()

    class Meta:
        model = api_models.Model
        fields = ('id', 'name', 'slug', 'year', 'make')


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.PaymentType
        fields = ('id', 'name', 'slug')
