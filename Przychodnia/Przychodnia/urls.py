from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cms/', admin.site.urls),
    path('przychodnia/', include('przychodnia_app.urls', namespace='przychodnia_app')),
    path('laboratorium/', include('laboratorium_app.urls', namespace='laboratorium_app')),
    path('', include('common.urls', namespace='common')),
]
