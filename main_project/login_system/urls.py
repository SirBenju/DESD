from django.contrib import admin
from django.urls import path
from login_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path("login", views.login, name="login"),
    path("test", views.test_database_connection, name="test"),
    path('register/', views.register, name='register'),
]
