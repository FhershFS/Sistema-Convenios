from django.test import TestCase
from django.contrib.auth.models import User, Group
from usuarios.forms import AgregarUsuarioAGrupo, UserRegisterForm


class TestFormUsuario(TestCase):

    def setUp(self):

        self.data = {
            "username": "usuariopruebas",
            "email": "correopruebas@hotmail.com",
            "password1": "clave123456",
            "password2": "clave123456",
            "first_name": "Eric",
            "last_name": "Castañeda"
        }

    def test_userRegister_form_valido(self):
        form = UserRegisterForm(self.data)
        self.assertTrue(form.is_valid)

    def test_user_username_null(self):
        self.data["username"] = None
        form = UserRegisterForm(self.data)
        self.assertFalse(form.is_valid())

    def test_user_username_requerido(self):
        self.data["username"] = ""
        form = UserRegisterForm(self.data)
        self.assertEqual(form.errors["username"], ['This field is required.'])

    def test_user_email_null(self):
        self.data["email"] = None
        form = UserRegisterForm(self.data)
        self.assertFalse(form.is_valid())

    def test_user_email_requerido(self):
        self.data["email"] = ""
        form = UserRegisterForm(self.data)
        self.assertEqual(form.errors["email"], ['This field is required.'])

    def test_user_password1_null(self):
        self.data["password1"] = None
        form = UserRegisterForm(self.data)
        self.assertFalse(form.is_valid())

    def test_user_password1_requerido(self):
        self.data["password1"] = ""
        form = UserRegisterForm(self.data)
        self.assertEqual(form.errors["password1"], ['This field is required.'])

    def test_user_password2_null(self):
        self.data["password1"] = None
        form = UserRegisterForm(self.data)
        self.assertFalse(form.is_valid())

    def test_user_password2_requerido(self):
        self.data["password2"] = ""
        form = UserRegisterForm(self.data)
        self.assertEqual(form.errors["password2"], ['This field is required.'])

    def test_user_passwords_iguales(self):
        self.data["password1"] = "clave123"
        self.data["password2"] = "clave123"
        form = UserRegisterForm(data=self.data)
        self.assertTrue(form.is_valid())
        self.assertEqual(
            form.cleaned_data["password2"], form.cleaned_data["password1"])

    def test_user_first_name_null(self):
        self.data["first_name"] = None
        form = UserRegisterForm(self.data)
        self.assertFalse(form.is_valid())

    def test_user_first_name_requerido(self):
        self.data["first_name"] = ""
        form = UserRegisterForm(self.data)
        self.assertEqual(form.errors["first_name"], [
                         'This field is required.'])

    def test_user_last_name_null(self):
        self.data["last_name"] = None
        form = UserRegisterForm(self.data)
        self.assertFalse(form.is_valid())

    def test_user_last_name_requerido(self):
        self.data["last_name"] = ""
        form = UserRegisterForm(self.data)
        self.assertEqual(form.errors["last_name"], ['This field is required.'])

    def test_user_email_formato_incorrecto(self):
        self.data["email"] = "correo"
        form = UserRegisterForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_user_email_formato_correcto(self):
        self.data["email"] = "correo_correcto@hotmail.com"
        form = UserRegisterForm(data=self.data)
        self.assertTrue(form.is_valid())


class TestFormAgregarUsuarioAGrupo(TestCase):
    def setUp(self):
        self.grupo_admin = Group.objects.create(name='admin')
        self.grupo_mov = Group.objects.create(name='movilidad')
        self.grupo_vinc = Group.objects.create(name='vinculacion')

        self.usuario = User.objects.create(username='fherfelixs',)
        self.usuario.set_password('DarkRay8')
        self.usuario.save()

        # Assign the Group to the User
        self.usuario.groups.add(self.grupo_admin)

        # Refresh the User instance to get the updated group information
        self.usuario.refresh_from_db()

        self.client.login(username='fherfelixs', password='DarkRay8')

        self.user = self.create_user()

    def create_user(self, username='UsuarioPruebaPermisosAmin', password='testpass', first_name="Usuario Prueba", last_name="Admin"):
        return User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)

    def test_form_valid_data(self):
        form_data = {'groups': self.grupo_admin.id}
        form = AgregarUsuarioAGrupo(data=form_data)

        self.assertTrue(form.is_valid())
        usuario = form.save(self.usuario, commit=False)
        self.assertEqual(usuario.groups.first(), self.grupo_admin)

    def test_form_invalid_data(self):
        form_data = {'groups': 999}
        form = AgregarUsuarioAGrupo(data=form_data)

        self.assertFalse(form.is_valid())

    def test_form_save_commit(self):
        self.user.groups.set([2])
        form_data = {'groups': self.grupo_admin.id}
        form = AgregarUsuarioAGrupo(data=form_data)

        form.is_valid()

        form.save(user=self.user, commit=True)
        query = User.objects.filter(
            username=self.user.username, groups=self.grupo_admin)
        self.assertTrue(query.exists())

    def test_form_save_no_commit(self):
        self.user.groups.set([2])
        form_data = {'groups': self.grupo_admin.id}
        form = AgregarUsuarioAGrupo(data=form_data)

        form.is_valid()

        form.save(user=self.user, commit=False)
        self.assertFalse(User.objects.filter(
            username=self.user.username, groups=self.grupo_mov).exists())

    def tearDown(self):
        self.usuario.delete()
        self.grupo_admin.delete()
