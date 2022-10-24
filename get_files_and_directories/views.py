from pathlib import Path

from django.http import JsonResponse
from django.views import View

import os

from config.config import *


class GetFilesAndDirectories(View):

    def get(self, request, *args, **kwargs):
        url = ROOT_DIR
        data = get_files_and_dirs(url)
        return JsonResponse(data)


def get_files_and_dirs(path: Path, data=None):
    if data is None:
        data = {'data': []}
    hidden_files_and_dirs = {
        'venv': 'venv',
        '.git': '.git',
        '.idea': '.idea',
        '__pycache__': '__pycache__'
    }
    for path in path.iterdir():
        if path.name in hidden_files_and_dirs:
            continue
        new_dict = dict()
        new_dict['name'] = path.name
        new_dict['time'] = os.stat(path)[-1]
        if path.is_dir():
            new_dict['type'] = 'folder'
            data['data'].append(new_dict)

            get_files_and_dirs(path=path, data=data)
        else:
            new_dict['type'] = 'file'
            data['data'].append(new_dict)
    return data
