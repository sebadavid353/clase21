from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.login_request, name='login'),
]

urlpatterns += staticfiles_urlpatterns ()


