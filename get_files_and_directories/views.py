from django.http import JsonResponse
from django.views import View

import os

from config.settings import BASE_DIR


class GetFilesAndDirectories(View):

    def get(self, request, *args, **kwargs):
        data = _get_files()
        return JsonResponse(data)


def _get_files():
    path = BASE_DIR
    data = {'data': []}
    a = os.listdir(path)
    dict_of_types = {'text': '.txt', 'pdf': '.pdf', 'python': '.py', 'sqlite': '.sqlite3'}
    for file in a:
        new_dict = dict()
        new_dict['name'] = os.path.basename(file)
        new_dict['time'] = os.stat(file)[7]
        if os.path.splitext(file)[1] in dict_of_types.values():
            new_dict['type'] = os.path.splitext(file)[1]
        elif os.path.splitext(file)[1] not in dict_of_types:
            f = os.listdir(file)
            if '__init__.py' in f:
                new_dict['type'] = 'folder'
            else:
                continue
        data['data'].append(new_dict)
    return data
