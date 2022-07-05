from menu.models import Nation, Foodlist
from rest_framework import serializers


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = ['nation', 'foodmenu']

    foodmenu = serializers.SerializerMethodField()

    def get_foodmenu(self, obj):
        print(obj)
        foods = Foodlist.objects.filter(pk=obj.id)
        serializer = FoodlistSerializer(foods, many=True)
        return serializer.data


class FoodlistSerializer(serializers.ModelSerializer):
    nation = serializers.StringRelatedField()

    class Meta:
        model = Foodlist
        fields = ['foodname', 'nation']
