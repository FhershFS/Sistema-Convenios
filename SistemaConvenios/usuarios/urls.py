from django.urls import path
from usuarios import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('administrar/', views.administrar_usuarios, name="administrar"),
    path('editar_usuario/<int:user_id>/',
         views.editar_usuario, name="editar_usuario"),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),


]
