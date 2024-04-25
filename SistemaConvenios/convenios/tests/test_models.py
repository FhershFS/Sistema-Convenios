from django.test import TestCase
from convenios.models import PersonaTramite, UnidadAcademica, Convenio
from django.core.exceptions import ValidationError


class TestModelsConvenio (TestCase):

    def setUp(self):
        self.persona = PersonaTramite.objects.create(nombre="PruebaPersona1")
        self.unidad = UnidadAcademica.objects.create(nombre="PruebaUnidad1")

        self.convenio = Convenio(
            numero="666",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

    def test_return_object_convenio(self):
        self.convenio.full_clean()
        self.convenio.save()
        self.assertEqual(Convenio.objects.first().numero,
                         self.convenio.__str__())

    def test_return_object_persona(self):
        self.assertEqual(PersonaTramite.objects.first().nombre,
                         self.persona.__str__())

    def test_return_object_unidad(self):
        self.assertEqual(UnidadAcademica.objects.first().nombre,
                         self.unidad.__str__())

    def test_persona_nombre_requerido(self):
        persona = PersonaTramite()
        with self.assertRaises(ValidationError):
            persona.full_clean()

    def test_persona_nombre_not_null(self):
        persona = PersonaTramite(nombre=None)
        with self.assertRaises(ValidationError):
            persona.full_clean()

    def test_unidad_nombre_requerido(self):
        unidad = UnidadAcademica()
        with self.assertRaises(ValidationError):
            unidad.full_clean()

    def test_unidad_nombre_not_null(self):
        unidad = UnidadAcademica(nombre=None)
        with self.assertRaises(ValidationError):
            unidad.full_clean()

    def test_convenio_numero_requerido(self):
        convenio = Convenio(
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )
        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_convenio_numero_not_null(self):
        convenio = Convenio(
            numero=None,
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_convenio_tipo_required(self):
        convenio = Convenio(
            numero="666",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_convenio_tipo_not_null(self):
        convenio = Convenio(
            numero="666",
            tipo=None,
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_convenio_persona_requerido(self):
        convenio = Convenio(
            numero="666",
            tipo="Diversas Instituciones",
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_convenio_persona_not_null(self):
        convenio = Convenio(
            numero="666",
            tipo="Diversas Instituciones",
            persona_tramito=None,
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_convenio_unidad_requerido(self):
        convenio = Convenio(
            numero="666",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
        )

        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_convenio_unidad_not_null(self):
        convenio = Convenio(
            numero="666",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=None
        )

        with self.assertRaises(ValidationError):
            convenio.full_clean()

    def test_clave_convenio_duplicada(self):
        self.convenio.full_clean()
        self.convenio.save()
        convenio2 = Convenio(
            numero="666",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_persona_maxima_longitud(self):
        persona = PersonaTramite(nombre="a"*101)

        with self.assertRaises(ValidationError):
            persona.full_clean()

    def test_unidad_maxima_longitud(self):
        unidad = UnidadAcademica(nombre="a"*101)

        with self.assertRaises(ValidationError):
            unidad.full_clean()

    def test_convenio_numero_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6"*11,
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_tipo_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales"*10,
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_objeto_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            objeto_convenio="a"*501
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_tipo_institucion_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            tipo_institucion="a"*151
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_tipo_representante_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            representante_legal="a"*101
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_recurso_economico_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            recurso_economico="a"*11
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_PNT_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            PNT="a"*11
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_PDF_estado_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            PDF_estado="a"*11
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_visto_bueno_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            visto_bueno="a"*11
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_documento_editable_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            documento_editable="a"*11
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_firmado_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            firmado="a"*11
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_estado_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            estado="a"*11
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()

    def test_convenio_ubicacion_maxima_longitud(self):
        convenio2 = Convenio(
            numero="6",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            ubicacion="a"*101
        )

        with self.assertRaises(ValidationError):
            convenio2.full_clean()
