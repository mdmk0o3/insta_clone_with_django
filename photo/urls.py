"""config URL Configuration

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
from django.urls import path
from .views import PhotoCreate, PhotoDelete, PhotoDetail, PhotoList, PhotoUpdate, PhotoLike, PhotoFavorite
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

app_name = 'photo'

urlpatterns = [
    path("create/", PhotoCreate.as_view(), name = 'create'),
    path("like/<int:photo_id>", PhotoLike.as_view(), name = 'like'),
    path("favorite/<int:photo_id>", PhotoFavorite.as_view(), name = 'favorite'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name = 'update'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name = 'delete'),
    path("detail/<int:pk>/", PhotoDetail.as_view(), name = 'detail'),
    path("", PhotoList.as_view(), name = 'index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
