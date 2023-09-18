"""
URL configuration for ddd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, reverse_lazy
from ninja import NinjaAPI

from lib.controller import load_api
from lib.error import catch_errors
from lib.renderer import ORJSONRenderer

URL_NAMESPACE = "sjbat-api"

api = NinjaAPI(
    renderer=ORJSONRenderer(),
    # version="1"
    urls_namespace=URL_NAMESPACE,
)


catch_errors(api)
load_api(api)



# api.post("/test")(lambda request: "Hello World!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
