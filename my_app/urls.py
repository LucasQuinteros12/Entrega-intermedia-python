from django.urls import path

from my_app import views

app_name = "my_app"
urlpatterns = [
    path("cars", view=views.cars, name="car-list"),
    path("car/add", view=views.create_cars, name="car-add"),
    path("accesorys", view=views.accesorys, name="accesory-list"),
    path("accesory/add", view=views.create_accesory, name="accesory-add"),
    path("clothes", view=views.clothes, name="clothe-list"),
    path("clothe/add", view=views.create_clothe, name="clothe-add"),
]