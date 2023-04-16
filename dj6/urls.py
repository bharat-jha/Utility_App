
from django.contrib import admin
from django.urls import path,include
from todo import views
from accounts import views as acc_views
from word import views as wd_views
from . import  settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("home/",acc_views.home,name="home1"),
    path("",views.addTodo, name="home"),
    path("delete/<int:id>/",views.todo_delete, name="delete"), 
    path("update/<int:id>/",views.todo_update,name="update"),
    path('notes/',include('notes.urls')),
    path('cal/', include('cal.urls')),
    path('lookup/', wd_views.home,name='lookup'),
    path('search/', wd_views.search,name='Search'),
    path('dashboard/', wd_views.dashboard,name='Dashboard'),
    
]

urlpatterns = urlpatterns +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

