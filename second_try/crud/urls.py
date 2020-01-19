from django.urls import path,include


urlpatterns = [
    path('/home', views.printin,name='printin'),
]
