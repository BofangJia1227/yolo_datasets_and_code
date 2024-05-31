import os

# 图片文件夹路径
img_folder = 'C:/Users/han_jp/Desktop/image/image'
# txt文件夹路径
txt_folder = 'C:/Users/han_jp/Desktop/image/label'

# 获取图片文件夹下所有jpg文件的文件名（不包含后缀）
img_files = [os.path.splitext(f)[0] for f in os.listdir(img_folder) if f.endswith('.jpg') or f.endswith('.JPG')]
# 获取txt文件夹下所有txt文件的文件名（不包含后缀）
txt_files = [os.path.splitext(f)[0] for f in os.listdir(txt_folder) if f.endswith('.txt')]

# 找到没有对应txt文件的图片
no_match = [img for img in img_files if img not in txt_files]

# 打印结果
for img in no_match:
    print(f'Image file {img}.jpg does not have a corresponding txt file.')
