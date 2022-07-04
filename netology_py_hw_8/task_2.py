import requests

from pprint import pprint
from my_token import TOKEN


class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    # Метод создает необходимые заголовки с токеном для доступа к диску
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # Метод возвращает словарь с перечнем файлов на диске, просто для теста
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        params = {'offset': 1, 'limit': 3}
        response = requests.get(files_url, headers=headers, params=params)
        return response.json()

    # Метод получает ссылку и место необходимые для загрузки на диск
    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        # Параметр "overwrite" - перезапись файла если он там уже есть
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        if response.status_code == 200:
            print("Cсылка получена")
        else:
            print('Ошибка! Код:', response.status_code)
        return response.json()

    # Метод загружает файл через полученную ссылку
    def upload_file_to_disk(self, disk_file_path, filename):
        # Под ключом "href" находится неободимая ссылка, поэтому методом get для словаря достает значение
        href = self.get_upload_link(disk_file_path=disk_file_path).get("href", "")
        # Запрос на сохранение файла по полученной ссылке 
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print(f"Файл '{filename}' успешно загружен")
        else:
            print('Ошибка! Код:', response.status_code)


if __name__ == '__main__':
    # Путь сохранения файла на Яндекс диске в существующую директорию netology
    path_to_file = 'netology/hw_8_task_2_test.txt'
    # Имя файла на локальном диске
    filename = 'test.txt'
    # Переменная где хранится токен полученный на https://yandex.ru/dev/disk/poligon/
    token = TOKEN

    uploader = YaUploader(token)
    # result = uploader.get_files_list()['items']
    # pprint(result)
    uploader.upload_file_to_disk(path_to_file, filename)
