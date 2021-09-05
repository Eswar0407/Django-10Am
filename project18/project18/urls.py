"""project18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app18 import views
from project18 import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('save_student/',views.saveStudent,name='save_student'),
    path('open_admin/',views.showAdmin,name='admin'),
    path('del_candidate/<int:student_number>', views.delCandidate, name='delete_candidate'),
    path('update_candidate/', views.updateCandidate, name='update_candidate'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

