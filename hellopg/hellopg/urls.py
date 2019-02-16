"""hellopg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from pg import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.homeView),
    url(r'^pgAroundKhrar/', views.pgAroundKhrarView.as_view()),
    url(r'^pgInKhrar/', views.pgInKhrarView.as_view()),
    url(r'^upload/', views.uploadView),
    url(r'^(?P<pk>\d+)/$', views.roomDetailView.as_view()),
    url(r'^edit/(?P<pk>\d+)/$', views.editPostView,name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeletePostView,name='delete'),
    url(r'^tiffin/', views.tiffinView),
    url(r'^team/', views.teamView),
    url(r'^gallary1/', views.gallary1View),
    url(r'^gallary2/', views.gallary2View),
    url(r'^about/', views.aboutView),
    url(r'^contact/', views.contactView),
    url(r'^logout/', views.logoutView),
    url(r'^signup/', views.signUpView),
    url(r'^ownerPGaroundKhrarList/', views.ownerPGaroundKhrarListView),
    url(r'^ownerPGinKhrarList/', views.ownerPGinKhrarListView),
    url(r'^dashboard/', views.dashboardView,name='dashboard'),
    url(r'^profile/', views.userProfileView),
    url(r'^profile/', views.userProfileView),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
