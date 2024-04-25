from django.test import TestCase
from convenios.models import PersonaTramite, UnidadAcademica, Convenio
from convenios.forms import ConvenioForm


class TestFormConvenio(TestCase):

    def setUp(self):

        self.persona = PersonaTramite.objects.create(nombre="PruebaPersona1")
        self.unidad = UnidadAcademica.objects.create(nombre="PruebaUnidad1")

        self.data = {
            "numero": "123",
            "tipo": "Diversas Instituciones",
            "persona_tramito": self.persona,
            "unidad_academica": self.unidad
        }

        self.convenio = Convenio.objects.create(
            numero="666",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

    # Alta convenio

    def test_convenio_form_valido(self):
        form = ConvenioForm(self.data)
        self.assertTrue(form.is_valid)

    def test_convenio_numero_null(self):
        self.data["numero"] = None
        form = ConvenioForm(self.data)
        self.assertFalse(form.is_valid())

    def test_convenio_numero_requerido(self):
        self.data["numero"] = ""
        form = ConvenioForm(self.data)
        self.assertEqual(form.errors["numero"], ['This field is required.'])

    def test_convenio_categoria_null(self):
        self.data["tipo"] = None
        form = ConvenioForm(self.data)
        self.assertFalse(form.is_valid())

    def test_convenio_categoria_requerido(self):
        self.data["tipo"] = ""
        form = ConvenioForm(self.data)
        self.assertEqual(form.errors["tipo"], ['This field is required.'])

    def test_convenio_persona_null(self):
        self.data["persona_tramito"] = None
        form = ConvenioForm(self.data)
        self.assertFalse(form.is_valid())

    def test_convenio_persona_requerido(self):
        self.data["persona_tramito"] = ""
        form = ConvenioForm(self.data)
        self.assertEqual(form.errors["persona_tramito"], [
                         'This field is required.'])

    def test_convenio_unidad_null(self):
        self.data["unidad_academica"] = None
        form = ConvenioForm(self.data)
        self.assertFalse(form.is_valid())

    def test_convenio_unidad_requerido(self):
        self.data["unidad_academica"] = ""
        form = ConvenioForm(self.data)
        self.assertEqual(form.errors["unidad_academica"], [
                         'This field is required.'])

    # Editar convenio

    def test_editar_convenio_numero_null(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["numero"] = None
        form = ConvenioForm(self.data, instance=convenio)
        self.assertFalse(form.is_valid())

    def test_editar_convenio_numero_unico(self):
        convenio = Convenio.objects.create(
            numero="900",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )
        convenio2 = Convenio.objects.get(pk=self.convenio.id)
        self.data["numero"] = convenio.numero
        form = ConvenioForm(self.data, instance=convenio2)
        self.assertFalse(form.is_valid())

    def test_editar_convenio_numero_requerido(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["numero"] = ""
        form = ConvenioForm(self.data, instance=convenio)
        self.assertEqual(form.errors["numero"], ['This field is required.'])

    def test_editar_convenio_categoria_null(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["tipo"] = None
        form = ConvenioForm(self.data, instance=convenio)
        self.assertFalse(form.is_valid())

    def test_editar_convenio_categoria_requerido(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["tipo"] = ""
        form = ConvenioForm(self.data, instance=convenio)
        self.assertEqual(form.errors["tipo"], ['This field is required.'])

    def test_editar_convenio_persona_null(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["persona_tramito"] = None
        form = ConvenioForm(self.data, instance=convenio)
        self.assertFalse(form.is_valid())

    def test_editar_convenio_persona_requerido(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["persona_tramito"] = ""
        form = ConvenioForm(self.data, instance=convenio)
        self.assertEqual(form.errors["persona_tramito"], [
                         'This field is required.'])

    def test_editar_convenio_unidad_null(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["persona_tramito"] = None
        form = ConvenioForm(self.data, instance=convenio)
        self.assertFalse(form.is_valid())

    def test_editar_convenio_unidad_requerido(self):
        convenio = Convenio.objects.get(pk=self.convenio.id)
        self.data["unidad_academica"] = ""
        form = ConvenioForm(self.data, instance=convenio)
        self.assertEqual(form.errors["unidad_academica"], [
                         'This field is required.'])
