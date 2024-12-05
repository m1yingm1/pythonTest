import shutil
import os

# 定义源文件夹和目标文件夹
source = 'path/to/a'  # 替换为实际路径
destination = 'path/to/b'  # 替换为实际路径

# 确保目标文件夹存在
if not os.path.exists(destination):
    os.makedirs(destination)

# 拷贝文件夹及其内容
shutil.copytree(source, destination, dirs_exist_ok=True)

print(f'文件夹 {source} 已成功拷贝到 {destination}')