from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetDatabase
from rest_framework.routers import SimpleRouter
from hydcdac import viewset


router = SimpleRouter()
router.register(r'cdachyd', viewset.HydcdacViewset, basename='')

'''
snippet_list = viewset.HydcdacViewset.as_view({
    'get': 'list',
    'post': 'create'
})
'''
emp_add= viewset.Hydcdacup.as_view({
    'put': 'update',
    'post':'create',
    'get': 'list'
})
urlpatterns = [
    
     path('db_data_fetch/<str:packagename>',GetDatabase.as_view(),name="database_fetch"),
     path('emp_add',emp_add),
    #path('/snippet_list',snippet_list)
]+router.get_urls()

urlpatterns = format_suffix_patterns(urlpatterns)

























 #path('insert/',views.SendDatabase.as_view(),name="sending")
 #path('<str:package_name>/', views.SnippetList.as_view(),name='snippets_list'),
#path('snippets/<int:pk>/', views.snippet_detail),
#path('snippets/<int:pk>/',views.SnippetDetail.as_view(),name='snippets_details'),