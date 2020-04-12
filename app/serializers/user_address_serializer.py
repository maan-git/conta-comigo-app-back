from rest_framework import serializers
from app.models.user_address import UserAddress
from app.models.neighborhood import Neighborhood
from app.models.city import City
from app.models.state import State


class NeighborhoodSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ("id", "description")


class CitySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "description")


class StateSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("id", "description")


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        exclude = ("created",)
        depth = 3

    neighborhood = NeighborhoodSimpleSerializer()
    city = CitySimpleSerializer(source="neighborhood.city")
    state = StateSimpleSerializer(source="neighborhood.city.state")
