from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# 为不同类别分配颜色
COLORS = {
    'person': (255, 0, 0),  # 红色
    'car': (0, 255, 0),  # 绿色
    'dog': (0, 0, 255),  # 蓝色
    'cat': (255, 255, 0),  # 黄色
    'bear': (255, 165, 0),  # 橙色
    'skis': (255, 192, 203),  # 粉色
    # 可以根据需要继续添加其他类别
}

# YOLOv8 模型加载
model = YOLO(r'D:\原桌面\ultralytics-main\runs\detect\train11\weights\best.pt')  #


def detect_objects(image_path, filename):
    # 读取图像
    img = Image.open(image_path)
    img_cv = np.array(img)  # 将图像转换为 numpy 数组，YOLO 接受的是 ndarray 格式

    # 使用 YOLOv8 模型进行推断
    results = model(img_cv)

    # 获取检测框、标签和置信度
    boxes = results[0].boxes  # 获取检测框信息
    labels = results[0].names  # 获取标签名
    confidences = boxes.conf  # 获取置信度

    # 可视化目标检测结果
    draw = ImageDraw.Draw(img)

    # 设置字体（如果没有字体文件，字体大小和样式需要调整）
    font = ImageFont.load_default()  # 可以换成合适的字体文件

    # 遍历每个检测框，使用左上角和右下角坐标（xyxy）
    for i, box in enumerate(boxes.xyxy):  # 使用 xyxy 直接获取框的坐标
        xmin, ymin, xmax, ymax = box.tolist()  # 获取边界框的四个坐标
        label = labels[int(boxes.cls[i])]  # 获取标签（类别）
        confidence = confidences[i].item()  # 获取置信度

        # 为每个类别分配不同颜色
        color = COLORS.get(label, (255, 255, 255))  # 默认为白色，如果找不到类别

        # 绘制边界框
        draw.rectangle([xmin, ymin, xmax, ymax], outline=color, width=3)

        # 创建背景色以增强文本可读性
        text = f"{label} ({confidence * 100:.2f}%)"

        # 使用 textbbox 计算文本大小
        text_bbox = draw.textbbox((xmin, ymin - 10), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]  # 文本宽度
        text_height = text_bbox[3] - text_bbox[1]  # 文本高度

        # 创建背景色填充
        draw.rectangle([xmin, ymin - text_height, xmin + text_width, ymin], fill=color)

        # 绘制类别和置信度
        draw.text((xmin, ymin - text_height), text, fill="white", font=font)

    # 保存处理后的图像
    result_image_path = os.path.join('uploads', f"result_{filename}")
    img.save(result_image_path)

    return result_image_path

# from ultralytics import YOLO
# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
# import os
#
# # 为不同类别分配颜色
# COLORS = {
#     'person': (255, 0, 0),  # 红色
#     'car': (0, 255, 0),  # 绿色
#     'dog': (0, 0, 255),  # 蓝色
#     'cat': (255, 255, 0),  # 黄色
#     'bear': (255, 165, 0),  # 橙色
#     'skis': (255, 192, 203),  # 粉色
#     # 可以根据需要继续添加其他类别
# }
#
# # YOLOv8 模型加载
# model = YOLO('yolov8n.pt')  # 假设你已经下载了 yolov8n.pt 模型
#
#
# def detect_objects(image_path, filename):
#     # 读取图像
#     img = Image.open(image_path)
#     img_cv = np.array(img)  # 将图像转换为 numpy 数组，YOLO 接受的是 ndarray 格式
#
#     # 使用 YOLOv8 模型进行推断
#     results = model(img_cv)
#
#     # 获取检测框、标签和置信度
#     boxes = results[0].boxes  # 获取检测框信息
#     labels = results[0].names  # 获取标签名
#     confidences = boxes.conf  # 获取置信度
#
#     # 可视化目标检测结果
#     draw = ImageDraw.Draw(img)
#
#     # 设置字体（如果没有字体文件，字体大小和样式需要调整）
#     font = ImageFont.load_default()  # 可以换成合适的字体文件
#
#     # 遍历每个检测框，使用左上角和右下角坐标（xyxy）
#     for i, box in enumerate(boxes.xyxy):  # 使用 xyxy 直接获取框的坐标
#         xmin, ymin, xmax, ymax = box.tolist()  # 获取边界框的四个坐标
#         label = labels[int(boxes.cls[i])]  # 获取标签（类别）
#         confidence = confidences[i].item()  # 获取置信度
#
#         # 为每个类别分配不同颜色
#         color = COLORS.get(label, (255, 255, 255))  # 默认为白色，如果找不到类别
#
#         # 绘制边界框
#         draw.rectangle([xmin, ymin, xmax, ymax], outline=color, width=3)
#
#         # 创建背景色以增强文本可读性
#         text = f"{label} ({confidence * 100:.2f}%)"
#
#         # 使用 textbbox 计算文本大小
#         text_bbox = draw.textbbox((xmin, ymin - 10), text, font=font)
#         text_width = text_bbox[2] - text_bbox[0]  # 文本宽度
#         text_height = text_bbox[3] - text_bbox[1]  # 文本高度
#
#         # 创建背景色填充
#         draw.rectangle([xmin, ymin - text_height, xmin + text_width, ymin], fill=color)
#
#         # 绘制类别和置信度
#         draw.text((xmin, ymin - text_height), text, fill="white", font=font)
#
#     # 保存处理后的图像
#     result_image_path = os.path.join('uploads', f"result_{filename}")
#     img.save(result_image_path)
#
#     return result_image_path

# from ultralytics import YOLO
# from PIL import Image, ImageDraw
# import numpy as np
# import os
#
# # 为不同类别分配颜色
# COLORS = {
#     'person': (255, 0, 0),  # 红色
#     'car': (0, 255, 0),     # 绿色
#     'dog': (0, 0, 255),     # 蓝色
#     'cat': (255, 255, 0),   # 黄色
#     'bear': (255, 165, 0),  # 橙色
#     'skis': (255, 192, 203), # 粉色
#     # 可以根据需要继续添加其他类别
# }
#
# # YOLOv8 模型加载
# model = YOLO('yolov8n.pt')  # 假设你已经下载了 yolov8n.pt 模型
#
# def detect_objects(image_path, filename):
#     # 读取图像
#     img = Image.open(image_path)
#     img_cv = np.array(img)  # 将图像转换为 numpy 数组，YOLO 接受的是 ndarray 格式
#
#     # 使用 YOLOv8 模型进行推断
#     results = model(img_cv)
#
#     # 获取检测框、标签和置信度
#     boxes = results[0].boxes  # 获取检测框信息
#     labels = results[0].names  # 获取标签名
#     confidences = boxes.conf  # 获取置信度
#
#     # 可视化目标检测结果
#     draw = ImageDraw.Draw(img)
#
#     # 遍历每个检测框，使用左上角和右下角坐标（xyxy）
#     for i, box in enumerate(boxes.xyxy):  # 使用 xyxy 直接获取框的坐标
#         xmin, ymin, xmax, ymax = box.tolist()  # 获取边界框的四个坐标
#         label = labels[int(boxes.cls[i])]  # 获取标签（类别）
#         confidence = confidences[i].item()  # 获取置信度
#
#         # 为每个类别分配不同颜色
#         color = COLORS.get(label, (255, 255, 255))  # 默认为白色，如果找不到类别
#
#         # 绘制边界框
#         draw.rectangle([xmin, ymin, xmax, ymax], outline=color, width=3)
#
#         # 使用字体来绘制类别和置信度
#         text = f"{label} ({confidence*100:.2f}%)"
#         draw.text((xmin, ymin), text, fill=color)
#
#     # 保存处理后的图像
#     result_image_path = os.path.join('uploads', f"result_{filename}")
#     img.save(result_image_path)
#
#     return result_image_path

# from ultralytics import YOLO
# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
# import os
#
# # 为不同类别分配颜色
# COLORS = {
#     'person': (255, 0, 0),  # 红色
#     'car': (0, 255, 0),     # 绿色
#     'dog': (0, 0, 255),     # 蓝色
#     'cat': (255, 255, 0),   # 黄色
#     'bear': (255, 165, 0),  # 橙色
#     'skis': (255, 192, 203), # 粉色
#     # 可以根据需要继续添加其他类别
# }
#
# # YOLOv8 模型加载
# model = YOLO('yolov8n.pt')  # 假设你已经下载了 yolov8n.pt 模型
#
# def detect_objects(image_path, filename):
#     # 读取图像
#     img = Image.open(image_path)
#     img_cv = np.array(img)  # 将图像转换为 numpy 数组，YOLO 接受的是 ndarray 格式
#
#     # 使用 YOLOv8 模型进行推断
#     results = model(img_cv)
#
#     # 获取检测框、标签和置信度
#     boxes = results[0].boxes  # 获取检测框信息
#     labels = results[0].names  # 获取标签名
#     confidences = boxes.conf  # 获取置信度
#
#     # 可视化目标检测结果
#     draw = ImageDraw.Draw(img)
#
#     # 遍历每个检测框，使用左上角和右下角坐标（xyxy）
#     for i, box in enumerate(boxes.xyxy):  # 使用 xyxy 直接获取框的坐标
#         xmin, ymin, xmax, ymax = box.tolist()  # 获取边界框的四个坐标
#         label = labels[int(boxes.cls[i])]  # 获取标签（类别）
#         confidence = confidences[i].item()  # 获取置信度
#
#         # 为每个类别分配不同颜色
#         color = COLORS.get(label, (255, 255, 255))  # 默认为白色，如果找不到类别
#
#         # 绘制边界框
#         draw.rectangle([xmin, ymin, xmax, ymax], outline=color, width=3)
#
#         # 使用字体来绘制类别和置信度
#         text = f"{label} ({confidence*100:.2f}%)"
#         draw.text((xmin, ymin), text, fill=color)
#
#     # 保存处理后的图像
#     result_image_path = os.path.join('uploads', f"result_{filename}")
#     img.save(result_image_path)
#
#     return result_image_path
