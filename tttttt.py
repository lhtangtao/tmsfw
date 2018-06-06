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
    house_info_list_all = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find(name="tbody")
    for tr in tbody.find_all(name="tr"):
        house_info_list = []
        td = tr.find_all(name="td")[0]
        building = td.contents[1].string  # 楼栋号
        room_number = tr.find_all(name="div")[0]  # 第一个div是房号
        room_number = room_number.contents[0].string
        div2 = tr.find_all(name="div")[1]
        span_area = ""
        for span in div2.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            span_area = span_area + span
        div3 = tr.find_all(name="div")[2]
        span_inner_area = ""
        for span in div3.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            span_inner_area = span_inner_area + span
        div4 = tr.find_all(name="div")[3]
        span_housing_rate = ""
        for span in div4.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            span_housing_rate = span_housing_rate + span
        div5 = tr.find_all(name="div")[4]
        billet_unit_price = ""
        for span in div5.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            billet_unit_price = billet_unit_price + span
        div6 = tr.find_all(name="div")[5]
        decoration_price = ""
        for span in div6.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            decoration_price = decoration_price + span
        div7 = tr.find_all(name="div")[6]
        total_price = ""
        for span in div7.find_all(name="span"):
            span = (span["class"])
            span = to_num(span[0])
            total_price = total_price + span
        div8 = tr.find_all(name="div")[7]
        operation = div8.contents[0].string  # 操作 是否可以出手
        house_info_list.append(building)
        house_info_list.append(room_number)
        house_info_list.append(span_area)
        house_info_list.append(span_inner_area)
        house_info_list.append(span_housing_rate)
        house_info_list.append(billet_unit_price)
        house_info_list.append(decoration_price)
        house_info_list.append(total_price)
        house_info_list.append(operation)
        house_info_list_all.append(house_info_list)
        print("++++++++++++++++++++++++++++++++++++")
    return house_info_list_all


if __name__ == '__main__':
    # get_page_num()
    print get_village_info(
        "http://www.tmsf.com/newhouse/property_33_375419827_price.htm?isopen=&presellid=&buildingid=&area=&allprice=&housestate=&housetype=&page=3")
