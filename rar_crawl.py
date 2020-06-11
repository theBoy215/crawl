#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time : 2019/11/2 22:01
@Author : https://github.com/theBoy215/
@file: RarExtract.py
@time: 2019/11/2 22:01
@desc: 主要用于解决网页中存在的rar文件, 将指定内容读到内存里
'''

from io import BytesIO

import rarfile
import requests
from fake_useragent import UserAgent


class RarExtract():

    def __init__(self):
        self._headers = {
            "User-Agent": UserAgent().random
        }
        self.rarObj = None

    # 解析rar文件, 生成rarfile对象
    def parse(self, url):
        req = requests.get(url, headers=self._headers).content
        req = BytesIO(req)
        self.rarObj = rarfile.RarFile(req)
        return self.rarObj

    # 获取rar文件内容
    def info(self):
        name_ls = []
        for n in self.rarObj.infolist():
            name_ls.append(n.filename)
        return name_ls

    # 获取指定文件内容
    def content(self, name):
        f = self.rarObj.infolist()
        for n in f:
            if name in n.filename:
                with self.rarObj.open(n) as f1:
                    rf = BytesIO(f1.read())
                    return rf
