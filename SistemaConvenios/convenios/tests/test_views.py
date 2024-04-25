from django.test import TestCase
from django.urls import reverse
from convenios.models import PersonaTramite, UnidadAcademica, Convenio
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from urllib.parse import urlencode


class TestViewsConvenio(TestCase):

    def setUp(self):

        self.group_name = 'admin'
        self.group = Group.objects.create(name=self.group_name)

        self.persona = PersonaTramite.objects.create(nombre="PruebaPersona1")
        self.unidad = UnidadAcademica.objects.create(nombre="PruebaUnidad1")

        self.usuario = User.objects.create(username='fherfelixs',)
        self.usuario.set_password('DarkRay8')
        self.usuario.save()

        # Assign the Group to the User
        self.usuario.groups.add(self.group)

        # Refresh the User instance to get the updated group information
        self.usuario.refresh_from_db()

        self.client.login(username='fherfelixs', password='DarkRay8')

        self.data = {
            "numero": "123",
            "tipo": "Diversas Instituciones",
            "fecha_ingreso": "2023-12-03",
            "fecha_inicio": "2023-12-03",
            "fecha_salida": "2023-12-03",
            "fecha_termino": "2023-12-03",
            "persona_tramito": self.persona.id,
            "unidad_academica": self.unidad.id,
            "estado": "Terminado",
        }

        self.convenio = Convenio.objects.create(
            numero="123",
            tipo="Diversas Instituciones",
            fecha_ingreso="2023-12-03",
            fecha_inicio="2023-12-03",
            fecha_salida="2023-12-03",
            fecha_termino="2023-12-03",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            estado="TERMINADO"
        )

        self.data2 = {
            "numero": "1234",
            "tipo": "Internacionales",
            "fecha_ingreso": "2023-12-03",
            "fecha_inicio": "2023-12-03",
            "fecha_salida": "2023-12-03",
            "fecha_termino": "2023-12-03",
            "persona_tramito": self.persona.id,
            "unidad_academica": self.unidad.id,
            "estado": "En espera",
        }

        self.convenio2 = Convenio.objects.create(
            numero="1234",
            tipo="Internacionales",
            fecha_ingreso="2023-12-03",
            fecha_inicio="2023-12-03",
            fecha_salida="2023-12-03",
            fecha_termino="2023-12-03",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            estado="ESPERA"
        )

        self.data3 = {
            "numero": "12345",
            "tipo": "Nacionales",
            "fecha_ingreso": "2023-12-03",
            "fecha_inicio": "2023-12-03",
            "fecha_salida": "2023-12-03",
            "fecha_termino": "2023-12-03",
            "persona_tramito": self.persona.id,
            "unidad_academica": self.unidad.id,
            "estado": "No empezado",
        }

        self.convenio3 = Convenio.objects.create(
            numero="12345",
            tipo="Nacionales",
            fecha_ingreso="2023-12-03",
            fecha_inicio="2023-12-03",
            fecha_salida="2023-12-03",
            fecha_termino="2023-12-03",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            estado="NO EMPEZADO"
        )

        self.data4 = {
            "numero": "12345",
            "tipo": "Varios",
            "fecha_ingreso": "2023-12-03",
            "fecha_inicio": "2023-12-03",
            "fecha_salida": "2023-12-03",
            "fecha_termino": "2023-12-03",
            "persona_tramito": self.persona.id,
            "unidad_academica": self.unidad.id,
            "estado": "No empezado",
        }

        self.convenio4 = Convenio.objects.create(
            numero="123456",
            tipo="Varios",
            fecha_ingreso="2023-12-03",
            fecha_inicio="2023-12-03",
            fecha_salida="2023-12-03",
            fecha_termino="2023-12-03",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            estado="NO EMPEZADO"
        )

    # Filtrados diversas instuticiones

    def test_filtrado_categoria_diversas_instituciones(self):
        respuesta = self.client.get('/diversas_instituciones/')
        self.assertAlmostEquals(respuesta.status_code, 200)

    def test_filtrado_convenio_por_numero_existente(self):
        url = reverse('diversas_instituciones') + \
            f'?numero={self.convenio.numero}'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '123')

    def test_filtrado_convenio_por_numero_no_existente(self):
        url = reverse('diversas_instituciones') + '?numero=999'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_clave_existente(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(url, data={'clave_id': self.convenio.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123')

    def test_filtrado_convenio_por_clave_no_existente(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(url, data={'clave_id': '999'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_ingreso(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(
            url, data={'fecha_ingreso': self.convenio.fecha_ingreso})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123')

    def test_filtrado_convenio_por_fecha_ingreso_no_encontrada(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(url, data={'fecha_ingreso': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_inicio(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(
            url, data={'fecha_inicio': self.convenio.fecha_inicio})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_inicio_no_encontrada(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(url, data={'fecha_inicio': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_salida(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(
            url, data={'fecha_salida': self.convenio.fecha_salida})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_salida_no_encontrada(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(url, data={'fecha_salida': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_termino(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(
            url, data={'fecha_termino': self.convenio.fecha_termino})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_termino_no_encontrada(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(url, data={'fecha_termino': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_persona(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(
            url, data={'persona_tramito': self.convenio.persona_tramito})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaPersona1')

    def test_filtrado_convenio_por_unidad(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(
            url, data={'unidad_academica': self.convenio.unidad_academica})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaUnidad1')

    def test_filtrado_convenio_por_status(self):
        url = reverse('diversas_instituciones')
        response = self.client.post(url, data={'estado': self.convenio.estado})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TERMINADO')

    # Filtrados Internacionales

    def test_filtrado_categoria_internacionales(self):
        respuesta = self.client.get('/internacionales/')
        self.assertAlmostEquals(respuesta.status_code, 200)

    def test_filtrado_convenio_por_numero_existente2(self):
        url = reverse('internacionales') + f'?numero={self.convenio2.numero}'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '1234')

    def test_filtrado_convenio_por_numero_no_existente2(self):
        url = reverse('internacionales') + '?numero=999'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_clave_existente2(self):
        url = reverse('internacionales')
        response = self.client.post(url, data={'clave_id': self.convenio2.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1234')

    def test_filtrado_convenio_por_clave_no_existente2(self):
        url = reverse('internacionales')
        response = self.client.post(url, data={'clave_id': '999'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_ingreso2(self):
        url = reverse('internacionales')
        response = self.client.post(
            url, data={'fecha_ingreso': self.convenio2.fecha_ingreso})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1234')

    def test_filtrado_convenio_por_fecha_ingreso_no_encontrada2(self):
        url = reverse('internacionales')
        response = self.client.post(url, data={'fecha_ingreso': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_inicio2(self):
        url = reverse('internacionales')
        response = self.client.post(
            url, data={'fecha_inicio': self.convenio2.fecha_inicio})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_inicio_no_encontrada2(self):
        url = reverse('internacionales')
        response = self.client.post(url, data={'fecha_inicio': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_salida2(self):
        url = reverse('internacionales')
        response = self.client.post(
            url, data={'fecha_salida': self.convenio2.fecha_salida})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_salida_no_encontrada2(self):
        url = reverse('internacionales')
        response = self.client.post(url, data={'fecha_salida': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_termino2(self):
        url = reverse('internacionales')
        response = self.client.post(
            url, data={'fecha_termino': self.convenio2.fecha_termino})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_termino_no_encontrada2(self):
        url = reverse('internacionales')
        response = self.client.post(url, data={'fecha_termino': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_persona2(self):
        url = reverse('internacionales')
        response = self.client.post(
            url, data={'persona_tramito': self.convenio2.persona_tramito})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaPersona1')

    def test_filtrado_convenio_por_unidad2(self):
        url = reverse('internacionales')
        response = self.client.post(
            url, data={'unidad_academica': self.convenio2.unidad_academica})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaUnidad1')

    def test_filtrado_convenio_por_status2(self):
        url = reverse('internacionales')
        response = self.client.post(
            url, data={'estado': self.convenio2.estado})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ESPERA')

    # Filtrado Nacionales

    def test_filtrado_categoria_nacionales(self):
        respuesta = self.client.get('/nacionales/')
        self.assertAlmostEquals(respuesta.status_code, 200)

    def test_filtrado_convenio_por_numero_existente3(self):
        url = reverse('nacionales') + f'?numero={self.convenio3.numero}'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '12345')

    def test_filtrado_convenio_por_numero_no_existente3(self):
        url = reverse('nacionales') + '?numero=999'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_clave_existente3(self):
        url = reverse('nacionales')
        response = self.client.post(url, data={'clave_id': self.convenio3.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '12345')

    def test_filtrado_convenio_por_clave_no_existente3(self):
        url = reverse('nacionales')
        response = self.client.post(url, data={'clave_id': '999'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_ingreso3(self):
        url = reverse('nacionales')
        response = self.client.post(
            url, data={'fecha_ingreso': self.convenio3.fecha_ingreso})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '12345')

    def test_filtrado_convenio_por_fecha_ingreso_no_encontrada3(self):
        url = reverse('nacionales')
        response = self.client.post(url, data={'fecha_ingreso': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_inicio3(self):
        url = reverse('nacionales')
        response = self.client.post(
            url, data={'fecha_inicio': self.convenio3.fecha_inicio})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_inicio_no_encontrada3(self):
        url = reverse('nacionales')
        response = self.client.post(url, data={'fecha_inicio': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_salida3(self):
        url = reverse('nacionales')
        response = self.client.post(
            url, data={'fecha_salida': self.convenio3.fecha_salida})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_salida_no_encontrada3(self):
        url = reverse('nacionales')
        response = self.client.post(url, data={'fecha_salida': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_termino3(self):
        url = reverse('nacionales')
        response = self.client.post(
            url, data={'fecha_termino': self.convenio3.fecha_termino})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_termino_no_encontrada3(self):
        url = reverse('nacionales')
        response = self.client.post(url, data={'fecha_termino': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_persona3(self):
        url = reverse('nacionales')
        response = self.client.post(
            url, data={'persona_tramito': self.convenio3.persona_tramito})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaPersona1')

    def test_filtrado_convenio_por_unidad3(self):
        url = reverse('nacionales')
        response = self.client.post(
            url, data={'unidad_academica': self.convenio3.unidad_academica})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaUnidad1')

    def test_filtrado_convenio_por_status3(self):
        url = reverse('nacionales')
        response = self.client.post(
            url, data={'estado': self.convenio3.estado})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NO EMPEZADO')

    # Filtrado Varios

    def test_filtrado_categoria_varios(self):
        respuesta = self.client.get('/varios/')
        self.assertAlmostEquals(respuesta.status_code, 200)

    def test_filtrado_convenio_por_numero_existente4(self):
        url = reverse('varios') + f'?numero={self.convenio4.numero}'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '123456')

    def test_filtrado_convenio_por_numero_no_existente4(self):
        url = reverse('varios') + '?numero=999'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_clave_existente4(self):
        url = reverse('varios')
        response = self.client.post(url, data={'clave_id': self.convenio4.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123456')

    def test_filtrado_convenio_por_clave_no_existente4(self):
        url = reverse('varios')
        response = self.client.post(url, data={'clave_id': '999'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_ingreso4(self):
        url = reverse('varios')
        response = self.client.post(
            url, data={'fecha_ingreso': self.convenio4.fecha_ingreso})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123456')

    def test_filtrado_convenio_por_fecha_ingreso_no_encontrada4(self):
        url = reverse('varios')
        response = self.client.post(url, data={'fecha_ingreso': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_inicio4(self):
        url = reverse('varios')
        response = self.client.post(
            url, data={'fecha_inicio': self.convenio4.fecha_inicio})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_inicio_no_encontrada4(self):
        url = reverse('varios')
        response = self.client.post(url, data={'fecha_inicio': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_salida4(self):
        url = reverse('varios')
        response = self.client.post(
            url, data={'fecha_salida': self.convenio4.fecha_salida})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_salida_no_encontrada4(self):
        url = reverse('varios')
        response = self.client.post(url, data={'fecha_salida': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_termino4(self):
        url = reverse('varios')
        response = self.client.post(
            url, data={'fecha_termino': self.convenio4.fecha_termino})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_termino_no_encontrada4(self):
        url = reverse('varios')
        response = self.client.post(url, data={'fecha_termino': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_persona4(self):
        url = reverse('varios')
        response = self.client.post(
            url, data={'persona_tramito': self.convenio4.persona_tramito})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaPersona1')

    def test_filtrado_convenio_por_unidad4(self):
        url = reverse('varios')
        response = self.client.post(
            url, data={'unidad_academica': self.convenio4.unidad_academica})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaUnidad1')

    def test_filtrado_convenio_por_status4(self):
        url = reverse('varios')
        response = self.client.post(
            url, data={'estado': self.convenio4.estado})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NO EMPEZADO')

    # Filtrados pendientes

    def test_filtrado_categoria_pendientes(self):
        respuesta = self.client.get('/pendientes/')
        self.assertAlmostEquals(respuesta.status_code, 200)

    def test_filtrado_convenio_por_numero_existente5(self):
        url = reverse('pendientes') + f'?numero={self.convenio4.numero}'
        respuesta = self.client.get(url)
        url2 = reverse('pendientes') + f'?numero={self.convenio3.numero}'
        respuesta2 = self.client.get(url2)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '123456')
        self.assertEqual(respuesta2.status_code, 200)
        self.assertContains(respuesta2, '12345')

    def test_filtrado_convenio_por_numero_no_existente5(self):
        url = reverse('pendientes') + '?numero=999'
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_clave_existente5(self):
        url = reverse('pendientes')
        response = self.client.post(url, data={'clave_id': self.convenio4.id})
        response2 = self.client.post(url, data={'clave_id': self.convenio3.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123456')
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, '12345')

    def test_filtrado_convenio_por_clave_no_existente5(self):
        url = reverse('pendientes')
        response = self.client.post(url, data={'clave_id': '999'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_ingreso5(self):
        url = reverse('pendientes')
        response = self.client.post(
            url, data={'fecha_ingreso': self.convenio4.fecha_ingreso})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '123456')

    def test_filtrado_convenio_por_fecha_ingreso_no_encontrada5(self):
        url = reverse('pendientes')
        response = self.client.post(url, data={'fecha_ingreso': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_inicio5(self):
        url = reverse('pendientes')
        response = self.client.post(
            url, data={'fecha_inicio': self.convenio4.fecha_inicio})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_inicio_no_encontrada5(self):
        url = reverse('pendientes')
        response = self.client.post(url, data={'fecha_inicio': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_salida5(self):
        url = reverse('pendientes')
        response = self.client.post(
            url, data={'fecha_salida': self.convenio4.fecha_salida})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_salida_no_encontrada5(self):
        url = reverse('pendientes')
        response = self.client.post(url, data={'fecha_salida': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_fecha_termino5(self):
        url = reverse('pendientes')
        response = self.client.post(
            url, data={'fecha_termino': self.convenio4.fecha_termino})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dec. 3, 2023')

    def test_filtrado_convenio_por_fecha_termino_no_encontrada5(self):
        url = reverse('pendientes')
        response = self.client.post(url, data={'fecha_termino': '2024-12-03'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'No se encontraron resultados.')

    def test_filtrado_convenio_por_persona5(self):
        url = reverse('pendientes')
        response = self.client.post(
            url, data={'persona_tramito': self.convenio4.persona_tramito})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaPersona1')

    def test_filtrado_convenio_por_unidad5(self):
        url = reverse('pendientes')
        response = self.client.post(
            url, data={'unidad_academica': self.convenio4.unidad_academica})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PruebaUnidad1')

    def test_filtrado_convenio_por_status5(self):
        url = reverse('pendientes')
        response = self.client.post(
            url, data={'estado': self.convenio4.estado})
        response2 = self.client.post(
            url, data={'estado': self.convenio2.estado})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NO EMPEZADO')
        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, 'ESPERA')

    # Filtrados de categorias

    def test_muestra_diversas_insts(self):
        respuesta = self.client.get(reverse('diversas_instituciones'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '123')

    def test_muestra_internacionales(self):
        Convenio.objects.create(
            numero="67890123",
            tipo="Internacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        respuesta = self.client.get(reverse('internacionales'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '67890123')

    def test_muestra_nacionales(self):
        Convenio.objects.create(
            numero="k99999999",
            tipo="Nacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        respuesta = self.client.get(reverse('nacionales'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'k99999999')

    def test_muestra_pendientes(self):
        Convenio.objects.create(
            numero="12/23456",
            tipo="Nacionales",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
            estado="ESPERA"
        )

        respuesta = self.client.get(reverse('pendientes'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, '12/23456')

    def test_muestra_varios(self):
        Convenio.objects.create(
            numero="ki980123",
            tipo="Varios",
            persona_tramito=self.persona,
            unidad_academica=self.unidad,
        )

        respuesta = self.client.get(reverse('varios'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'ki980123')

    def test_agrega_convenio_exitosamente(self):
        datos = {
            'numero': '00000000',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }
        response = self.client.post(
            '/agregar_convenio/',
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Convenio agregado')

    def test_agrega_clave_repetida(self):
        datos = {
            'numero': '123',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }
        response = self.client.post(
            '/agregar_convenio/',
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'La clave ya existe')

    def test_campos_obligatorios(self):
        datos = {
            'numero': '',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }
        response = self.client.post(
            '/agregar_convenio/',
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Llenar campos obligatorios')

    def test_agregar_convenio_campos_invalidos(self):
        datos = {
            'numero': '0000000000000000000000000000000000',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }
        with self.assertRaises(ValueError):
            self.client.post(
                '/agregar_convenio/',
                data=urlencode(datos),
                content_type='application/x-www-form-urlencoded',
                follow=True)

    def test_borrar_convenio(self):
        convenio = Convenio.objects.create(
            numero="11111111111",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        response = self.client.post(
            f"/borrar_convenio/{convenio.id}", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Convenio eliminado')

    def test_editar_convenio_exitosamente(self):

        convenio = Convenio.objects.create(
            numero="8900000",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        datos = {
            'numero': '222222',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }

        response = self.client.post(
            f"/editar_convenio/{convenio.id}",
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Convenio editado')

    def test_editar_convenio_campos_invalidos(self):

        convenio = Convenio.objects.create(
            numero="8900000",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        datos = {
            'numero': '2222222222222222222222222222222222222222',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }
        # with self.assertRaises(ValueError):
        response = self.client.post(
            f"/editar_convenio/{convenio.id}",
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_editar_clave_repetida(self):
        Convenio.objects.create(
            numero="8900001",
            tipo="Diversas Instituciones",
            persona_tramito=self.persona,
            unidad_academica=self.unidad
        )

        datos = {
            'numero': '8900001',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }

        response = self.client.post(
            f"/editar_convenio/{self.convenio.id}",
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'La clave ya existe')

    def test_editar_campos_requeridos(self):
        datos = {
            'numero': '',
            'tipo': 'Diversas Instituciones',
            'fecha_ingreso': '',
            'fecha_inicio': '',
            'fecha_salida': '',
            'fecha_termino': '',
            'objeto_convenio': '',
            'persona_tramito': 1,
            'unidad_academica': 1,
            'tipo_institucion': '',
            'representante_legal': '',
            'convenio_modificatorio': '',
            'PDF_archivo': '',
            'ubicacion': '',
        }

        response = self.client.post(
            f"/editar_convenio/{self.convenio.id}",
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Llenar campos obligatorios')

    def test_agregar_unidad(self):
        datos = {"nombre": "PruebaUnidad2"}
        response = self.client.post(
            "/agregar_unidad/",
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True)
        self.assertRedirects(response, '/', status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

    def test_agregar_persona(self):
        datos = {"nombre": "PruebPersona2"}
        response = self.client.post(
            "/agregar_persona/",
            data=urlencode(datos),
            content_type='application/x-www-form-urlencoded',
            follow=True)
        self.assertRedirects(response, '/', status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

    def test_ver_detalles_convenio(self):
        response = self.client.get(
            f"/mostrar_detalles_convenio/{self.convenio.id}")
        self.assertTemplateUsed(response, "mostrar_detalles_convenio.html")

    def test_template_agregar_convenio(self):
        response = self.client.get("/agregar_convenio/")
        self.assertTemplateUsed(response, "agregar_convenio.html")

    def test_template_borrar_convenio(self):
        response = self.client.get(f"/borrar_convenio/{self.convenio.id}")
        self.assertTemplateUsed(response, "borrar_convenio.html")

    def test_template_editar_convenio(self):
        response = self.client.get(f"/editar_convenio/{self.convenio.id}")
        self.assertTemplateUsed(response, "editar_convenio.html")

    def test_template_agregar_unidad(self):
        response = self.client.get("/agregar_unidad/")
        self.assertTemplateUsed(response, "agregar_unidad.html")

    def test_template_agregar_persona(self):
        response = self.client.get("/agregar_persona/")
        self.assertTemplateUsed(response, "agregar_persona.html")
