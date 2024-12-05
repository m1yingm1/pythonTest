import os
import shutil

# 定义源文件夹和目标文件夹
source_folder = 'E:\code\python\pythonProject1\Game'  # 替换为实际路径
destination_folder = 'E:\code\python\pythonTest'  # 替换为实际路径

# 确保目标文件夹存在
os.makedirs(destination_folder, exist_ok=True)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.py'):  # 检查文件扩展名
        source_file = os.path.join(source_folder, filename)  # 源文件的完整路径
        destination_file = os.path.join(destination_folder, filename)  # 目标文件的完整路径
        shutil.copy(source_file, destination_file)  # 拷贝文件

print(f'所有 .py 文件已成功从 {source_folder} 拷贝到 {destination_folder}')