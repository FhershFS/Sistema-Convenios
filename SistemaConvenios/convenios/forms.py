from django import forms
from .models import Convenio, UnidadAcademica, PersonaTramite

CATEGORIAS_CONVENIO = [
    ("Diversas Instituciones", "Diversas Instituciones"),
    ("Internacionales", "Internacionales"),
    ("Nacionales", "Nacionales"),
    ("Varios", "Varios")
]

OPCIONES = [
    ("SI", "Sí"),
    ("NO", "No")
]

ESTADOS_CONVENIO = [
    ("TERMINADO", "Terminado"),
    ("ESPERA", "En espera"),
    ("NO EMPEZADO", "No empezado")
]


class ConvenioForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=CATEGORIAS_CONVENIO,
    )
    fecha_ingreso = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_inicio = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_salida = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_termino = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    objeto_convenio = forms.CharField(required=False, widget=forms.Textarea)
    recurso_economico = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=OPCIONES,
    )
    PNT = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=OPCIONES,
    )
    PDF_estado = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=OPCIONES,
    )
    visto_bueno = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=OPCIONES,
    )
    documento_editable = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=OPCIONES,
    )
    firmado = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=OPCIONES,
    )
    estado = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(),
        choices=ESTADOS_CONVENIO,
    )

    class Meta:
        model = Convenio
        fields = '__all__'


class UnidadAcademicaForm(forms.ModelForm):
    class Meta:
        model = UnidadAcademica
        fields = '__all__'


class PersonaTramiteForm(forms.ModelForm):
    class Meta:
        model = PersonaTramite
        fields = '__all__'


class MostrarDetallesConvenioForm(forms.ModelForm):
    class Meta:
        model = Convenio
        fields = '__all__'

        def __init__(self, *args, **kwargs):  # pragma: no cover
            super().__init__(*args, **kwargs)  # No hay pruebas en srs

            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
