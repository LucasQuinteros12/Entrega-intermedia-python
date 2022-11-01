
from django.contrib import messages
from django.shortcuts import render

from my_app.models import Car, Accesory, Clothe
from my_app.forms import CarForm, AccesoryForm, ClotheForm

def create_cars(request):
    if request.method == "POST":
        car_form = CarForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if car_form.is_valid():
            data = car_form.cleaned_data
            actual_objects = Car.objects.filter(
                brand=data["brand"], model=data["model"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El coche {data['brand']} - {data['model']} ya está creado",
                )
            else:
                car = Car(brand=data["brand"], model=data["model"])
                car.save()
                messages.success(
                    request,
                    f"Coche {data['brand']} - {data['model']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"cars": Car.objects.all()},
                template_name="my_app/car_list.html",
            )

    car_form = CarForm(request.POST)
    context_dict = {"form": car_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/car_form.html",)

def cars(request):
    return render(
        request=request,
        context={"cars": Car.objects.all()},
        template_name="my_app/car_list.html",
    )

def create_accesory(request):
    if request.method == "POST":
        accesory_form = AccesoryForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if accesory_form.is_valid():
            data = accesory_form.cleaned_data
            actual_objects = Accesory.objects.filter(
                name=data["name"] , type=data["type"], price=data["price"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El Accesorio {data['name']} - {data['type']} ya está creado",
                )
            else:
                accesory = Accesory(name=data["name"] , type=data["type"], price=data["price"])
                accesory.save()
                messages.success(
                    request,
                    f"Acesorio {data['name']} - {data['type']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"accesorys": Accesory.objects.all()},
                template_name="my_app/accesory_list.html",
            )

    accesory_form = AccesoryForm(request.POST)
    context_dict = {"form": accesory_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/accesory_form.html",)

def accesorys(request):
    return render(
        request=request,
        context={"accesorys": Accesory.objects.all()},
        template_name="my_app/accesory_list.html",
    )

def create_clothe(request):
    if request.method == "POST":
        clothe_form = ClotheForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if clothe_form.is_valid():
            data = clothe_form.cleaned_data
            actual_objects = Clothe.objects.filter(
                brand=data["brand"] , type=data["type"], size=data["size"], color=data["color"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La prenda {data['brand']} - {data['type']} - {data['size']} - {data['color']}  ya está creado",
                )
            else:
                clothe = Clothe(brand=data["brand"] , type=data["type"], size=data["size"], color=data["color"])
                clothe.save()
                messages.success(
                    request,
                    f"{data['type']} - {data['brand']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"clothes": Clothe.objects.all()},
                template_name="my_app/clothe_list.html",
            )

    clothe_form = ClotheForm(request.POST)
    context_dict = {"form": clothe_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/clothe_form.html",)

def clothes(request):
    return render(
        request=request,
        context={"clothes": Clothe.objects.all()},
        template_name="my_app/clothe_list.html",
    )