"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import SimpleRouter, Route

from recipe import views

class CustomBreedsRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        # Otras rutas personalizadas si las necesitas
    ]

router = CustomBreedsRouter()
router.register('dogs', views.DogsViewSet, basename='dogs')
router.register('breeds', views.BreedsViewSet, basename='breeds')

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
    path('answer/', views.AnswerView.as_view()),
]