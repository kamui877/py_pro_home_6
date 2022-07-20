import requests


def create_folder(token):
    host = 'https://cloud-api.yandex.net'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': 'test'}
    res = requests.put(f'{host}/v1/disk/resources', headers=headers, params=params)
    return res.status_code
