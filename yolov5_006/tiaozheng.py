import os
import shutil

from PIL import Image

def convert_resize_and_rename_images(input_folder, output_folder, prefix, target_size):
    """
    批量转换、重命名和调整文件夹中的图片并移动到新文件夹
    :param input_folder: 输入文件夹路径
    :param output_folder: 输出文件夹路径
    :param prefix: 新文件名的前缀
    :param target_size: 目标尺寸 (width, height)
    """
    if not os.path.exists(input_folder):
        print("输入文件夹不存在")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("输出文件夹已创建")

    # 获取输入文件夹中所有文件的列表
    files = os.listdir(input_folder)

    # 设置计数器
    count = 1

    # 遍历文件列表
    for file_name in files:
        # 构建旧文件的完整路径
        old_file_path = os.path.join(input_folder, file_name)

        # 检查文件是否为图片文件
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # 构建新的文件名
            new_file_name = f"{prefix}{count:04d}.jpg"

            # 构建新文件的完整路径
            new_file_path = os.path.join(output_folder, new_file_name)

            # 打开并转换图片格式为 JPG
            with Image.open(old_file_path) as img:
                img = img.convert("RGB")

                # 调整图片尺寸
                img = img.resize(target_size)

                img.save(new_file_path, "JPEG")

            # 更新计数器
            count += 1
        else:
            # 如果不是图片文件，则直接复制到新文件夹中
            new_file_path = os.path.join(output_folder, file_name)
            shutil.copy(old_file_path, new_file_path)

if __name__ == "__main__":
    input_folder = "F:\yolov_module\yolov5_006\cd\ceshi"  # 输入文件夹路径
    output_folder = "F:\yolov_module\yolov5_006\cd\ceshi01"  # 输出文件夹路径
    prefix = "ceshi"  # 新文件名的前缀
    target_size = (300, 300)  # 目标尺寸

    convert_resize_and_rename_images(input_folder, output_folder, prefix, target_size)
