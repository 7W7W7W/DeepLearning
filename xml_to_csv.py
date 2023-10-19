# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:21:19 2019

@author: LKY
"""
# 将xml文件整合到一个csv文件中

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

## xml文件的路径
os.chdir('./data/annotations/scratches')
path = 'C:/Users/Admin/Desktop/data/annotations/scratches' # 绝对路径
img_path = 'C:/Users/Admin/Desktop/data/images'

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):  #返回所有匹配的文件路径列表。
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
#            value = (root.find('filename').text,
#                     int(root.find('size')[0].text),
#                     int(root.find('size')[1].text),
#                     member[0].text,
#                     int(member[4][0].text),
#                     int(member[4][1].text),
#                     int(member[4][2].text),
#                     int(member[4][3].text)
#                     )
            value = (img_path +'/' + root.find('filename').text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text),
                     member[0].text
                     )
            xml_list.append(value)
    #column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    column_name = ['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'class']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

if __name__ == '__main__':
    image_path = path
    xml_df = xml_to_csv(image_path)
    ## 修改文件名称
    xml_df.to_csv('scratches.csv', index=None)
    print('Successfully converted xml to csv.')
