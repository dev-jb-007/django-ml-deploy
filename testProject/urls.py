
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('',include('basicConcepts.url')),
    path('admin/', admin.site.urls),
    path('',include('irisApp.url')),
    path('data',include('basicConcepts.url'))
]
