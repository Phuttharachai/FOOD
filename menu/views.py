from rest_framework import permissions, viewsets, mixins, status
from menu.models import Nation, Foodlist
from menu.serializers import NationSerializer, FoodlistSerializer
from rest_framework.response import Response


class FoodlistViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = Foodlist.objects.all()
    serializer_class = FoodlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwarg):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwarg):
        food = Foodlist.objects.filter(nation_id=kwarg['pk'])
        serializer = FoodlistSerializer(food, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = Nation.objects.all()
    serializer_class = NationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwarg):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwarg):
        nation = Foodlist.objects.filter(nation_id=kwarg['pk'])
        serializer = NationSerializer(nation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
