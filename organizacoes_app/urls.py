from django.urls import path, include
from rest_framework.routers import DefaultRouter
from organizacoes_app.views import OrganizacaoViewSet

router = DefaultRouter()
router.register(r'organizacoes', OrganizacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]