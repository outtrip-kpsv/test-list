"""testlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from main.views import list_workers, add_worker, edit_worker, delete_worker, list_departments_languages, add_department, add_language

urlpatterns = [
    # path('', include('main.urls', namespace='main')),
    path('', list_workers, name='list_workers'),
    path('admin/', admin.site.urls),
    path('add/worker/', add_worker, name='add_worker'),
    path('add/department/', add_department, name='add_department'),
    path('add/language/', add_language, name='add_language'),
    path('edit/<int:id_worker>', edit_worker, name='edit_worker'),
    path('delete/<int:id_worker>', delete_worker, name='delete_worker'),
    path('depandlangs/', list_departments_languages, name='list_departments_languages')


]
