from django.urls import path
from .views import *

app_name='main'

urlpatterns=[
    path('',home),
    path('ingredients/',ingredient),
    path('category/',category),
    path('recipes/',recipe),
    path('recipes/detail/<int:id>',recipeDetail),
]