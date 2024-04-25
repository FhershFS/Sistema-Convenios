from django.db import models
from django.core.validators import FileExtensionValidator

OPCIONES = [
    ("SI", "Sí"),
    ("NO", "No")
]

ESTADOS_CONVENIO = [
    ("TERMINADO", "Terminado"),
    ("ESPERA", "En espera"),
    ("NO EMPEZADO", "No empezado")
]

CATEGORIAS_CONVENIO = [
    ("Diversas Instituciones", "Diversas Instituciones"),
    ("Internacionales", "Internacionales"),
    ("Nacionales", "Nacionales"),
    ("Varios", "Varios")
]

# Create your models here.


class Convenio(models.Model):

    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=50, choices=CATEGORIAS_CONVENIO)
    # TODO Deben tener el formato YYYY-MM-DD
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    fecha_termino = models.DateField(blank=True, null=True)
    objeto_convenio = models.CharField(max_length=500, blank=True, null=True)
    persona_tramito = models.ForeignKey(
        "PersonaTramite", on_delete=models.SET("N/A"))
    # Si eliminamos a una unidad academica no queremos que se borren los convenios
    unidad_academica = models.ForeignKey(
        "UnidadAcademica", on_delete=models.SET("N/A"))
    tipo_institucion = models.CharField(max_length=150, blank=True, null=True)
    representante_legal = models.CharField(
        max_length=100, blank=True, null=True)
    recurso_economico = models.CharField(
        max_length=10, choices=OPCIONES, blank=True, null=True, default="NO")
    PNT = models.CharField(max_length=10, choices=OPCIONES,
                           blank=True, null=True, default="NO")

    # Si el pdf está subido o no
    # TODO auto actualizar cuando se haya subido el PDF
    PDF_estado = models.CharField(
        max_length=10, choices=OPCIONES, blank=True, null=True, default="NO")
    visto_bueno = models.CharField(
        max_length=10, choices=OPCIONES, blank=True, null=True, default="NO")
    documento_editable = models.CharField(
        max_length=10, choices=OPCIONES, blank=True, null=True, default="NO")
    firmado = models.CharField(
        max_length=10, choices=OPCIONES, blank=True, null=True, default="NO")
    estado = models.CharField(
        max_length=20, choices=ESTADOS_CONVENIO, blank=True, null=True, default="ESPERA")
    # TODO Definir la ruta de upload
    # Archivo del convenio modificatorio
    convenio_modificatorio = models.FileField(
        blank=True, null=True, upload_to="convenios_modificatorios", validators=[FileExtensionValidator(["pdf"])])
    # El archivo del pdf como tal
    PDF_archivo = models.FileField(blank=True, null=True, upload_to="convenios", validators=[
                                   FileExtensionValidator(["pdf"])])
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.numero
    # esto no se uso nunca

    def get_model_fields(self):  # pragma: no cover
        return self._meta.fields


"""
class ConvenioParticipantes(models.Model):
    convenio =  models.ForeignKey(Convenio, on_delete=models.SET("N/A"))
    participante = models.ForeignKey("Participantes", on_delete=models.SET("N/A"))
"""
"""
class Participantes(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre
"""


class UnidadAcademica(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class PersonaTramite(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
