from django.urls import path
from apps.usuario import views

app_name = 'usuario'
urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
 ]
