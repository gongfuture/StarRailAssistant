import datetime
import hashlib
import json
from pathlib import Path

map_path = Path(__file__).parent / 'map'
temp_path = Path(__file__).parent / 'temp'

map_list = []
temp_list = []

this_path = str(Path(__file__).parent)

for file in map_path.rglob('*'):
    if os.path.isfile(file):
        map_list.append({
            'path': str(file).replace(this_path, '').replace('\\', '/').lstrip('/'),
            'hash': hashlib.md5(file.read_bytes()).hexdigest()
        })

for file in temp_path.rglob('*'):
    if os.path.isfile(file):
        map_list.append({
            'path': str(file).replace(this_path, '').replace('\\', '/').lstrip('/'),
            'hash': hashlib.md5(file.read_bytes()).hexdigest()
        })

with open('map_list.json', 'w', encoding='utf-8') as f:
    json.dump(map_list, f, ensure_ascii=False, indent=2)

with open('temp_list.json', 'w', encoding='utf-8') as f:
    json.dump(temp_list, f, ensure_ascii=False, indent=2)

# 获取当前时间（UTC+8）
current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)

# 生成版本号
version = current_time.strftime("%Y%m%d%H%M%S")

# 创建版本号字典
version_dict = {
    "version": version
}

# 写入到version.json文件
with open("version.json", "w") as file:
    json.dump(version_dict, file)
