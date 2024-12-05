import os
import requests
import re
import json

# 创建王者语音总文件夹
if not os.path.exists('./王者语音'):
    os.mkdir('./王者语音')


# 主函数
def hero_wzry_voice():
    # UA伪装
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"}

    # 第一个请求头,需要得到[英雄的编号列表]和[英雄的名字列表]:
    herolist_json_url = 'https://pvp.qq.com/web201605/js/herolist.json'
    response1 = requests.get(url=herolist_json_url, headers=headers).text

    hero_id_list = re.findall('"ename": (.+?),', response1, re.S)  # 得到英雄的编号列表(乱序的
    hero_name_list = re.findall('"cname": "(.+?)"', response1, re.S)  # 得到英雄的名字列表(乱序的

    # 第二个请求头,需要得到所有英雄语音信息:
    voice_src_url = 'https://pvp.qq.com/zlkdatasys/data_zlk_lb.json'
    param = {
        'callback': 'createList'}
    response2 = requests.get(url=voice_src_url, headers=headers, params=param).text

    response2 = response2.replace('createList(', '').replace(')', '')  # 去掉不符合json格式的部分字符串数据
    json_dict = json.loads(response2)  # 将字符串json格式化变成字典
    hero = json_dict['yylb_34']  # 字典取值，得到所有英雄的语音信息

    for i in range(len(hero)):

        id_result = hero[i]['yxid_a7']  # 最终的所有英雄编号
        hero_index = hero_id_list.index(id_result)  # 中间过程,获取所有英雄名称对应的索引,很关键的一步！！！
        name_result = hero_name_list[hero_index]  # 最终所有英雄编号对应的所有英雄名称
        voice_list = hero[i]['yy_4e']  # 获得所有英雄的语音列表

        _path = "./王者语音/{}/".format(name_result)
        if not os.path.exists(_path):
            os.mkdir(_path)  # 创建次级文件夹，稍后以英雄的名字来命名

        for j in range(len(voice_list)):

            voice_text = voice_list[j]['yywa1_f2']  # 语音内容的文本
            voice_url = 'http:' + voice_list[j]['yyyp_9a']  # 语音mp3的网址(url)
            voice_response = requests.get(url=voice_url, headers=headers).content

            # 异常捕获,我选择若遇到异常则跳过,继续执行程序
            try:
                with open(_path + '/' + '[' + name_result + ']' + '-' + voice_text + '.mp3', 'wb') as f:
                    f.write(voice_response)  # 写入mp3文件
                    print('-----成功下载并保存语音-----')

            except OSError:
                continue

    print("*****王者荣耀英雄语音已全部爬取成功！*****")


if __name__ == "__main__":
    hero_wzry_voice()