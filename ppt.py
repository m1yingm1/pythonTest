import os
from pptx import Presentation
from pptx.util import Inches

# 创建一个新的 PowerPoint 演示文稿
presentation = Presentation()

# 添加一页幻灯片
slide_layout = presentation.slide_layouts[6]  # 选择一种布局（5: 空白布局）
slide = presentation.slides.add_slide(slide_layout)

# 添加文本框
text_box = slide.shapes.add_textbox(Inches(1), Inches(5.5), Inches(8), Inches(1))  # 文本框位置和大小
text_frame = text_box.text_frame
text_frame.text = "这里是您的文本"  # 替换为您想要添加的文本
# 得到该文件下的所有png图片
folderPath = "./hero_name/云缨"
for filename in os.listdir(folderPath):
    if filename.endswith(".jpg"):
        img_path = os.path.join(folderPath, filename)
        # 添加图片
        left = Inches(1)  # 图片左边距
        top = Inches(1)  # 图片上边距
        scale = 0.5
        width = Inches(6)
        # width = Inches(1920 / 96 * scale)  # 图片宽度
        height = Inches(882 / 96 * scale)  # 图片高度
        slide.shapes.add_picture(img_path, left, top)
        break

# 保存演示文稿
presentation.save('output.pptx')  # 输出文件名
print("演示文稿已生成！")
