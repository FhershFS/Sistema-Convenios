from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.urls import reverse


class TestViewsConvenio(TestCase):

    def setUp(self):
        self.grupo_admin = Group.objects.create(name='admin')
        self.grupo_mov = Group.objects.create(name='movilidad')
        self.grupo_vinc = Group.objects.create(name='vinculacion')

        self.usuario = User.objects.create(username='fherfelixs',)
        self.usuario.set_password('DarkRay8')
        self.usuario.save()

        self.usuario.groups.add(self.grupo_admin)

        self.usuario.refresh_from_db()

        self.client.login(username='fherfelixs', password='DarkRay8')

    def test_register_view(self):

        response = self.client.post(
            '/usuarios/register/', data={'username': self.usuario.username, 'password': self.usuario.password})
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):

        self.client.login(username=self.usuario.username,
                          password=self.usuario.password)

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_administrar_usuarios_view(self):

        self.client.login(username=self.usuario.username,
                          password=self.usuario.password)

        response = self.client.get(reverse('administrar'))
        self.assertEqual(response.status_code, 200)

    def test_editar_usuario_view(self):
        self.client.login(username=self.usuario.username,
                          password=self.usuario.password)

        test_user = User.objects.create_user(
            username='testView', password='contraTest', first_name='Usuario Prueba', last_name="View")

        response = self.client.post(reverse('editar_usuario', args=[test_user.id]), {
                                    'some_form_data': 'value'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get(
            reverse('editar_usuario', args=[test_user.id]))
        self.assertEqual(response.status_code, 200)
