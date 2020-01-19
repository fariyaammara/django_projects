from django.urls  import path
from . import views


urlpatterns = [
    path('', views.printin,name='printin'),
]
