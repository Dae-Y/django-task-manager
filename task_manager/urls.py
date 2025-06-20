# Author: Daehwan Yeo 19448288
# Purpose: For WAF Assignment, urls
# Reference: Lec 2, 3 slides, Lab 2, 3
#            Used to fix Django Admin frontend crashing
#            https://wiki.imindlabs.com.au/dev/web/be/1_django/8_troubleshooting/
# Last mod: 21/03/2025

from django.contrib import admin
from django.urls import path, include

# To fix Admin Frontend breaking when DEBUG=False
from django.urls import re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks_app.urls')),
]


# To fix Admin Frontend breaking
if settings.DEBUG is False:
    urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})]
    
    
# Custom error handlers in lec 3 slides
handler400 = 'tasks_app.views.error_400'
handler403 = 'tasks_app.views.error_403'
handler404 = 'tasks_app.views.error_404'
handler500 = 'tasks_app.views.error_500'