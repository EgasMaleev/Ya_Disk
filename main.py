from pprint import pprint
import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_dict = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_dict.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")



TOKEN = "AQAAAABM9tR2AADLW4FNSpmMiEJ8qiX2_dNy4RY"
if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    file_name = input("Введите имя файла вместе с расширением, если в той же директории где и исполняющий файл или его абсолютный путь: ")
    a = file_name.split('\\')[-1]
    file_path_in_disk = f"/{a}"
    ya.upload_file_to_disk(file_path_in_disk, file_name)