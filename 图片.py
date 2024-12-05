import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号
skin_names = list(map(lambda x: x['skin_name'], herolist.json()))


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        # 创建文件夹
        folderPath = "./hero_name/" + hero_name[i]
        if not os.path.exists(folderPath):
            os.mkdir(folderPath)  # 创建文件夹
        # 进入创建好的文件夹
        # os.chdir(folderPath)

        skin_name = skin_names[i].split('|')
        # 正在下载第几个
        print('正在下载第' + str(i + 1) + '个')
        i += 1
        for k in range(len(skin_name) + 1):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                # 如果存在就不下载了
                if not os.path.exists(folderPath + '/' + skin_name[k - 1] + '.jpg'):
                    open(folderPath + '/' + skin_name[k - 1] + '.jpg', 'wb').write(im.content)  # 写入文件


if not os.path.exists('./hero_name'):
    os.mkdir('./hero_name')

#记录运行时间
import time
# 记录开始时间
start_time = time.time()

downloadPic()

# 记录结束时间
end_time = time.time()
# 计算并打印总耗时
total_time = end_time - start_time
print(f"下载完成，总耗时: {total_time:.2f} 秒")