#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=tmsfw 
#author=lhtangtao
#time=2018/5/30 23:14
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=添加描述信息
"""
import urllib2

from bs4 import BeautifulSoup

from infos import Info
from tools import to_num


def get_village_page_num(url):
    """
    获取本小区的房子数量的页面总数
    :param url:
    :return:int类型
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    title = soup.find_all("div", class_='spagenext')
    return int(title[0].contents[1].string.split("/")[1].split()[0])


def get_village_info(url):
    house_info_list = []
    house_info = Info()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find(name="tbody")
    for tr in tbody.find_all(name="tr"):
        td = tr.find_all(name="td")[0]
        building = td.contents[1].string  # 楼栋号
        # for div in tr.find_all(name="div"): # 这里 第一个div是房号，第二个div是建筑面积 第三个div是套内建筑面积，第四个是得房率 第五个是毛坯单价 第六个是装修家 第七个是总价 第八个是操作状态
        div1 = tr.find_all(name="div")[0]  # 第一个div是房号
        div1 = div1.contents[0].string
        div2 = tr.find_all(name="div")[1]  # 第二个div是建筑面积
        span_area = ""
        for span in div2.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            span_area = span_area + span
        # print(span_area)  # 建筑面积
        div3 = tr.find_all(name="div")[2]  # 第二个div是建筑面积
        span_inner_area = ""
        for span in div3.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            span_inner_area = span_inner_area + span
        # print(span_inner_area) # 套内面积
        div4 = tr.find_all(name="div")[3]  # 第二个div是建筑面积
        span_housing_rate = ""
        for span in div4.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            span_housing_rate = span_housing_rate + span
        print(span_housing_rate)  # 得房率
        print("++++++++++++++++++++++++++++++++++++")

    # for title in soup.find_all(name='tr'):
    #     print title
    #     print("++++++++++++++++++++++++++++++++++++++")
    #     # for tr in title.find_all("tr", class_="adTr"):
    #     #     print tr
    #     #     print("++++++++++++++++++++++++++++++++++++++")
    return house_info_list


if __name__ == '__main__':
    # get_page_num()
    print get_village_info(
        "http://www.tmsf.com/newhouse/property_33_511129767_price.htm?isopen=&presellid=&buildingid=&area=&allprice=&housestate=&housetype=&page=8")
