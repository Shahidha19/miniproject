# complaint_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('complaist/', include('complaint.urls')),
    path('complaint',include('complaint.urls'))
]
