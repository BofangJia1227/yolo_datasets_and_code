import xml.etree.ElementTree as ET
import pickle
import os
import shutil
from os import listdir, getcwd
from os.path import join
sets = ['train', 'trainval']
classes = ['cat','dog']
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
def convert_annotation(image_id):
    in_file = open('all_xml/%s.xml' % (image_id))
    out_file = open('all_labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
wd = getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists('all_labels/'):
        os.makedirs('all_labels/')
    image_ids = open('ImageSets/%s.txt' % (image_set)).read().strip().split()
    image_list_file = open('images_%s.txt' % (image_set), 'w')
    labels_list_file=open('labels_%s.txt'%(image_set),'w')
    for image_id in image_ids:
        image_list_file.write('%s.png\n' % (image_id))
        labels_list_file.write('%s.txt\n'%(image_id))
        convert_annotation(image_id) #如果标签已经是txt格式，将此行注释掉，所有的txt存放到all_labels文件夹。
    image_list_file.close()
    labels_list_file.close()


def copy_file(new_path, path_txt, search_path, file_format=None):
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    with open(path_txt, 'r') as lines:
        filenames_to_copy = set(line.rstrip() for line in lines)
    for root, _, filenames in os.walk(search_path):
        for filename in filenames:
            if filename in filenames_to_copy:
                if file_format and filename.endswith(file_format):
                    shutil.copy(os.path.join(root, filename), new_path)


#按照划分好的训练文件的路径搜索目标，并将其复制到yolo格式下的新路径
#按照划分好的训练文件的路径搜索目标，并将其复制到yolo格式下的新路径
copy_file('./images/train/','./images_train.txt','./all_images', 'png')
copy_file('./images/val/','./images_trainval.txt','./all_images', 'png')
copy_file('./labels/train/','./labels_train.txt','./all_labels')
copy_file('./labels/val/','./labels_trainval.txt','./all_labels')
