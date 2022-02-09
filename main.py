from pprint import pprint
import requests

from ya_disk import YandexDisk

TOKEN = "AQAAAABM9tR2AADLW4FNSpmMiEJ8qiX2_dNy4RY"
if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    file_path = str(input())
    path = f"'{file_path}'"
    print(file_path)
    print(r'''C:\Users\Егор\PycharmProjects\pythonProject2\landomnii_file.txt''')
    ya.upload_file_to_disk(file_path, file_path)
