from django.contrib import admin
from menu.models import Foodlist, Nation


@admin.register(Foodlist)
class FoodlistTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Nation)
class NationTypeAdmin(admin.ModelAdmin):
    pass
