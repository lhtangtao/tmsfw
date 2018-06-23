#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=tmsfw 
#author=lhtangtao
#time=2018/5/31 01:31
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=小区页面
"""
import urllib2

from bs4 import BeautifulSoup

from sql import insert_info, update_info
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
    id_num = 1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    location = soup.find(id_="districtname")
    print  location
    village_name = soup.find(class_='buidname colordg').contents[0].string.split()[0]  # 获取小区的名字
    other_name = soup.find(class_="extension famwei ft14 mgr10").find(class_="color-33").contents[0].string  # 获取小区推广名
    tbody = soup.find(name="tbody")
    for tr in tbody.find_all(name="tr"):
        td = tr.find_all(name="td")[0]
        building = td.contents[1].string  # 楼栋号
        url_dest = tr.find_all(class_="adTr")[1].find("a")["href"]
        url_dest = "http://www.tmsf.com/" + url_dest  # 每个房产的具体链接地址
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
        insert_info("ID", id_num)
        update_info("village", village_name, id_num)
        update_info("other_name", other_name, id_num)
        update_info("building", building, id_num)
        update_info("room", room_number, id_num)
        update_info("area", span_area, id_num)
        update_info("inner_area", span_inner_area, id_num)
        update_info("rate", span_housing_rate, id_num)
        update_info("billet_unit_price", billet_unit_price, id_num)
        update_info("decoration_price", decoration_price, id_num)
        update_info("total_price", total_price, id_num)
        update_info("operation", operation, id_num)
        update_info("url_address", url_dest, id_num)
        id_num = id_num + 1
    return

