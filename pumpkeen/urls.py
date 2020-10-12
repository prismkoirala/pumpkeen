"""pumpkeen URL Configuration

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
from django.urls import path, include
from billing.views import printing_page, settings_view, edit_oil

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('billing.urls')),

    path('print/', printing_page, name="printing_page" ),
    path('settings/', settings_view, name="settings"),
    path('edit-oil/<id>', edit_oil, name="edit_oil" )
]
