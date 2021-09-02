"""SunWavesDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from clients.views import create_client_view, home_view, search_view, add_options_view, search_results_view, delete_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-client/', create_client_view, name='create-client'),
    path('home/', home_view, name='home'),
    path('search/', search_view, name='search'),
    path('add-options/', add_options_view, name='add-options'),
    path('results/<str:ind>/<str:pos>/<str:res>/<int:exp>/<str:sort>/', search_results_view, name='results'),
    path('delete/<int:id>/', delete_view, name='delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
