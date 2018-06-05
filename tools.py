#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=tmsfw 
#author=lhtangtao
#time=2018/6/5 23:35
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=工具类
"""


def to_num(str_source):
    if str_source == "numberone":
        str_source = 1
    elif str_source == "numbertwo":
        str_source = 2
    elif str_source == "numberthree":
        str_source = 3
    elif str_source == "numberfour":
        str_source = 4
    elif str_source == "numberfive":
        str_source = 5
    elif str_source == "numbersix":
        str_source = 6
    elif str_source == "numberseven":
        str_source = 7
    elif str_source == "numbereight":
        str_source = 8
    elif str_source == "numbernine":
        str_source = 9
    elif str_source == "numberzero":
        str_source = 0
    elif str_source == "numberdor":
        str_source = "."
    return str(str_source)
