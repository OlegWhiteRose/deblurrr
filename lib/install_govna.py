
import os
import requests
from tqdm import tqdm

def download_file(session, url, save_path):
    response = session.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    with open(save_path, 'wb') as file:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=save_path) as pbar:
            for data in response.iter_content(chunk_size=8192):
                file.write(data)
                pbar.update(len(data))

TARGET_DIR = '.'
FILENAME = "GoPro.zip"

if not os.path.exists(os.path.join(TARGET_DIR, FILENAME)):
    print("Начинается загрузка датасета (около 5.5 ГБ). Пожалуйста, подождите...")
    session = requests.Session()
    file_url = 'https://titan.gml-team.ru:5003/fsdownload/zFoCt5HPQ/GoPro.zip'
    session.get(file_url)
    download_file(session, file_url, os.path.join(TARGET_DIR, FILENAME))