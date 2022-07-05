from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu import views

router = DefaultRouter()
router.register(r'foodlists', views.FoodlistViewSet)
router.register(r'nations', views.NationViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
