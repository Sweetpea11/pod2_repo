from django.urls import path
from . import views # the period stands for the file we are in

urlpatterns = [
    # this route serves up sandwich homepage
    path('', views.sandwich, name='sandwich'),
    # sandwich/ingredients/<str:ingredient_type>
    path('ingredients/<str:ingredient_type>', views.ingredients_list, name='ingredients_list'),
    # sandwich/random
    path('random', views.sandwich_generator, name='sandwich_generator'),
    # sandwich/menu
    path('menu', views.menu, name='menu')
]