import os
import requests
from concurrent.futures import ThreadPoolExecutor

# 获取英雄列表的 URL
url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表 json 文件

# 转换为 json 格式
herolist_json = herolist.json()
hero_name = list(map(lambda x: x['cname'], herolist_json))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist_json))  # 提取英雄的编号
skin_names = list(map(lambda x: x['skin_name'], herolist_json))


# 下载单个皮肤图片的函数
def download_skin_image(hero_id, skin_name, folder_path, skin_index):
    # 拼接 URL
    image_url = f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_id}/{hero_id}-bigskin-{skin_index}.jpg'
    response = requests.get(image_url)

    if response.status_code == 200:
        # 保存图片
        image_path = os.path.join(folder_path, f"{skin_name}.jpg")
        if not os.path.exists(image_path):
            with open(image_path, 'wb') as f:
                f.write(response.content)
                # print(f"下载完成: {image_path}")
    # else:
    #     print(f"未找到图片: {image_url}")


# 下载所有英雄的皮肤
def download_all_skins():
    folderPath='./hero_name'
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

    for i, hero_id in enumerate(hero_number):
        # 创建文件夹
        folder_path = os.path.join(folderPath, hero_name[i])
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)  # 创建文件夹

        skin_names_list = skin_names[i].split('|')
        # print(f'正在下载第 {i + 1} 个: {hero_name[i]}')
        print(f'正在下载第 {i + 1} 个')

        # 使用线程池下载皮肤
        with ThreadPoolExecutor() as executor:
            for k in range(len(skin_names_list) + 1):
                skin_name = skin_names_list[k - 1] if k > 0 else 'default'  # 默认皮肤名称
                executor.submit(download_skin_image, hero_id, skin_name, folder_path, k)

#记录运行时间
import time
# 记录开始时间
start_time = time.time()
download_all_skins()
# 记录结束时间
end_time = time.time()
# 计算并打印总耗时
total_time = end_time - start_time
print(f"下载完成，总耗时: {total_time:.2f} 秒")