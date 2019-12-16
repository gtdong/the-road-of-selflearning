
from django.conf.urls import url,include
# from api import views
from django.contrib import admin
import xadmin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/',xadmin.site.urls),
    url(r'^api/', include('api.urls')),
    # url(r'^asset/',views.asset)
    # url(r'^api/', include('api.urls')),
]
