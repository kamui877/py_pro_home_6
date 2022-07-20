import requests
import unittest
from yd import create_folder


token = 'Ваш токен'

class TestYD(unittest.TestCase):
    def test_create_folder(self):
        #Проверка на создание папки
        self.assertEqual(create_folder(token), 201)
        host = 'https://cloud-api.yandex.net'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': 'test'}
        resp = requests.get(f'{host}/v1/disk/resources', headers=headers, params=params)
        #Проверка на наличие новой папки
        self.assertEqual(resp.status_code, 200)

    def test_create_foldeer2(self):
        #Папка уже существует
        self.assertEqual(create_folder(token), 409)

