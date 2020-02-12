from django.contrib import admin
from django.urls import path
from irisapp import views as irisview
from houseapp import views as houseapp
urlpatterns = [
    path('', houseapp.index),
    path('api/species', irisview.api_species),
    path('admin/', admin.site.urls),
]
