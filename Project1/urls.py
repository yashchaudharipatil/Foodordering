from django.contrib import admin
from django.urls import path
from home.views import home
from vege.views import recipes

urlpatterns = [
    path('', home, name="home"),
    path('recipes/', recipes, name="recipes"),  # Update 'recipe' to 'recipes' here
    path('admin/', admin.site.urls),
]
