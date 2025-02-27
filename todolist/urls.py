"""
URL configuration for todolist project.

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
from django.urls import path
from django.views.generic import TemplateView
from list.views import index, monday, tuesday, wednesday, thursday, friday, saturday, sunday

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('monday/', monday, name= 'Понедельник'),
    path('tuesday/', tuesday, name= 'Вторник'),
    path('wednesday/', wednesday, name= 'Среда'),
    path('thursday/', thursday, name= 'Четверг'),
    path('friday/', friday, name= 'Пятница'),
    path('saturday/', saturday, name= 'Суббота'),
    path('sunday/', sunday, name= 'Воскресенье')

]
