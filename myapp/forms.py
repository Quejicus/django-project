from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Nombre de la tarea", max_length=200)
    description = forms.CharField(
        label="Descripción de la tarea", widget=forms.Textarea, required=False
    )
