# materials/urls.py
from django.urls import path
from .views import MaterialCreateView, MaterialRetrieveView, MaterialSearchView, AdvancedMaterialPropertyView, HomeView

urlpatterns = [
    path('material/', MaterialCreateView.as_view(), name='material-create'),
    path('material/<int:id>/', MaterialRetrieveView.as_view(), name='material-retrieve'),
    path('search/', MaterialSearchView.as_view(), name='material-search'),
    path('material/<int:id>/advanced-property/', AdvancedMaterialPropertyView.as_view(), name='advanced-material-property'),
    path('home/', HomeView.as_view(), name='Home-View')
]
