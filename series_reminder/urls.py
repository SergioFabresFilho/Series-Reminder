from django.contrib import admin
from django.urls import path, include

import core.urls
import series.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(core.urls, namespace='core')),
    path('series/', include(series.urls, namespace='series')),
]
