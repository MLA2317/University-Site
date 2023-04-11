"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

urlpatterns = [   # i18 ni urlpatternsga qoshsak barchasi tarjima qilinadi
    path('admin/', admin.site.urls),

    # local app
    path('', RedirectView.as_view(pattern_name='main:index')), #patern_name - bu v1/ ga birdaniga otvoradi kak indexga
    path('', include('app.main.urls', namespace='main')),
    path('account/', include('app.account.urls', namespace='account')),
    path('blog/', include('app.blog.urls', namespace='blog')),
    path('course/', include('app.course.urls', namespace='course'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
