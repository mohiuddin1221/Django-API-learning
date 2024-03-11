"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from rest_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('topuinfo/',views.Topu_views),
    #path('topuinfo/<int:pk>', views.Topu_instance),
    #path('topucretae/',views.topu_create),
    #path('topucretae/<int:pk>',views.topu_create),
    #path('topuclass', views.Topuclassbaseview.as_view()),
    #path('topuclass/<int:pk>', views.Topuclassbaseview.as_view())
    #path('topulist',views.TopuListView.as_view()),
    #path('topulist1',views.TopuretriveView.as_view()),
    #path('topulist1/<int:pk>',views.TopuretriveView.as_view()),
    path('topu2',views.topushortlistcreate.as_view()),
    path('topu3/<int:pk>',views.topu_cre_up_del.as_view())
   
    
         
]
