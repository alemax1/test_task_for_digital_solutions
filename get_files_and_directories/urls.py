from django.urls import path

from get_files_and_directories.views import *

urlpatterns = [
    path('api/meta', GetFilesAndDirectories.as_view())
]
