from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(
        label="Nombre de la tarea",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    description = forms.CharField(
        label="Descripción de la tarea",
        widget=forms.Textarea(attrs={"class": "input"}),
        required=False,
    )


class CreateNewProject(forms.Form):
    name = forms.CharField(
        label="Nombre del proyecto",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
