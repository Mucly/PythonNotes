# -*- coding: utf8 -*-
#!/usr/bin/env python
# 爬取国家地理的图片

import os
import requests
from bs4 import BeautifulSoup

os.makedirs('./tmp', exist_ok=True)

img_dict = {}  # { img_path : img_content_by_byte }

MAIN_URL = "http://www.ngchina.com.cn/animals/"

req = requests.get(MAIN_URL).content.decode('utf-8')
soup = BeautifulSoup(req, "html.parser")

# PART 1 找到所有ul元素
ul_elements = soup.find_all("ul", {"class": "img_list"})

# PART 2 找到所有ul元素下的img元素 -> 获取img元素 src节点内容（图片url）便于后续下载
for ul in ul_elements:
    img_elements = ul.find_all("img")
    for img_element in img_elements:
        img_url = img_element["src"]
        img_name = img_url.split("/")[-1]
        img_path = f"./tmp/{img_name}"

        # Way1 边下载边存硬盘，防止占用太多内存
        req = requests.get(img_url, stream=True)
        with open(img_path, "wb") as f:
            for chunk in req.iter_content(chunk_size=1024):
                f.write(chunk)

        # Way2 要下载的数据先通过内存缓存，然后一次性写入硬盘，易爆内存
        # req = requests.get(img_url).content
        # with open(img_path, "wb") as f:
        #     f.write(req)
