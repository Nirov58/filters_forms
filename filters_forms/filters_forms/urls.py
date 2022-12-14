"""filters_forms URL Configuration

The `urlpatterns` list routes URLs to filters_forms. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function filters_forms
    1. Add an import:  from my_app import filters_forms
    2. Add a URL to urlpatterns:  path('', filters_forms.home, name='home')
Class-based filters_forms
    1. Add an import:  from other_app.filters_forms import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('filters_forms_app.urls')),
    path('article/', include('filters_forms_app.urls'))
]
