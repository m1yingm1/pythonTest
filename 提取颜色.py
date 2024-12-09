from PIL import Image
import numpy as np
from collections import Counter


def get_dominant_color(image_path):
    # 打开图像
    image = Image.open(image_path)
    # 将图像转换为 RGB 模式
    image = image.convert('RGB')

    # 将图像数据转换为 numpy 数组
    pixels = np.array(image)
    # 将二维数组展平为一维
    pixels = pixels.reshape(-1, 3)

    # 计算颜色出现的频率
    color_counts = Counter(map(tuple, pixels))

    # 找到出现频率最高的颜色
    dominant_color = color_counts.most_common(1)[0][0]

    return dominant_color


# 示例用法
image_path = './hero_name/阿古朵/顽趣.jpg'  # 替换为您的图片路径
dominant_color = get_dominant_color(image_path)
print(f"占比最多的颜色 (RGB): {dominant_color}")