from django import forms


class CarForm(forms.Form):
    brand = forms.CharField(
        label="Marca:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "car-brand",
                "placeholder": "marca del coche",
                "required": "True",
            }
        ),
    )
    model = forms.IntegerField(
        label="Modelo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "car-model",
                "placeholder": "modelo",
                "required": "True",
            }
        ),
    )

class AccesoryForm(forms.Form):
    name = forms.CharField(
        label="Nombre:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accesory-name",
                "placeholder": "Nombre del accesorio",
                "required": "True",
            }
        ),
    )
    type = forms.CharField(
        label="Tipo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accesory-type",
                "placeholder": "Tipo de accesorio",
                "required": "True",
            }
        ),
    )
    price = forms.IntegerField(
        label="Precio:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accesory-price",
                "placeholder": "Precio",
                "required": "True",
            }
        ),
    )

class ClotheForm(forms.Form):
    brand = forms.CharField(
        label="Marca:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "clothe-brand",
                "placeholder": "Marca de la prenda. Ej: Nike",
                "required": "True",
            }
        ),
    )
    type = forms.CharField(
        label="Tipo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "clothe-type",
                "placeholder": "Tipo de Prenda. Ej: Camisa, Pantalón, etc.",
                "required": "True",
            }
        ),
    )
    size = forms.IntegerField(
        label="Talle:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "clothe-size",
                "placeholder": "Talle de la prenda. Ej: 38, 44, etc.",
                "required": "True",
            }
        ),
    )

    color= forms.CharField(
        label="Color:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "clothe-color",
                "placeholder": "Color de la prenda...",
                "required": "True",
            }
        ),
    )
