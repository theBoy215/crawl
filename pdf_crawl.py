#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time : 2019/11/2 21:54
@Author : https://github.com/theBoy215/
@file: PdfExtract.py
@time: 2019/11/2 21:54
@desc: 用于处理网页中出现的pdf文件
'''

from io import BytesIO

import pdfplumber
import requests
from fake_useragent import UserAgent


class PdfExtract():

    def __init__(self):
        self._header = {
            "User-Agent": UserAgent().random
        }

    # pdf抓取
    def start_url(self, url):
        """
        :param url:
        :return: 将pdf内容读取到内存中
        """
        try:
            if '.pdf' in url:
                # 获取pdf内容
                cont = requests.get(url, headers=self._header).content
                # 构建bytesIo对象
                cont = BytesIO(cont)
                return cont
        except Exception as e:
            print(e)

    # pdf内容解析  使用pdfplumber
    def parse(self, content):
        """
        :type 主要使用pdfplumber模块进行pdf内容解析
        :param content: 读取内存中的pdf数据
        :return: 返回字符串数据
        """
        # 加载pdf文件, 类型为二进制
        pdf = pdfplumber.load(content)
        targets = []  # 保存结果
        # 获取每一页的pdf内容
        for page in pdf.pages:
            # 获取当前页面的全部文本信息
            words = page.extract_text()
            # 对内容进行清洗
            word = words.replace(' ', '').replace('\n', '')
            targets.append(word)
        # 关闭pdf资源
        pdf.close()
        return ''.join(targets)
