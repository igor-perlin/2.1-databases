"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phones import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', phones.views.index),
    # path('catalog/', phones.views.show_catalog, name='catalog'),
    # path('catalog/<slug:slug>/', phones.views.show_product, name='phone'),
    path('', views.index, name='index'),
    path('catalog/', views.show_catalog, name='show_catalog'),
    path('catalog/<str:slug>/', views.show_product, name='show_product'),
    path('images/<path:path>', serve, {'document_root': settings.STATICFILES_DIRS[0]}),

]

# Настройте обслуживание статических файлов только в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,  # Используйте STATIC_URL из настроек
        document_root=settings.STATICFILES_DIRS[0],  # Указываем директорию для статических файлов
    )

    # Добавьте обслуживание изображений из директории /images/
    urlpatterns += static(
        '/images/',
        document_root=settings.STATICFILES_DIRS[1],  # Указываем директорию для изображений
    )
# if settings.DEBUG:
#     urlpatterns += static(
#         prefix='/static/',  # Указываем URL-префикс для статических файлов
#         document_root=settings.STATICFILES_DIRS[0],  # Указываем директорию для статических файлов
#     )