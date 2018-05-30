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


def get_village_href(url):
    """
    :param url:输入url，随后获取这个页面的所有一房一价页面的url信息
    :return:list url信息
    """
    village_id_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    for title in soup.find_all('div', class_="build_txt2"):
        village_id_list.append("http://www.tmsf.com" + str(title.contents[1]["href"]).replace("dynamic", "price"))
    return village_id_list


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


if __name__ == '__main__':
    # get_page_num()
    print get_village_page_num(
        "http://www.tmsf.com/newhouse/property_33_511129767_price.htm?isopen=&presellid=&buildingid=&area=&allprice=&housestate=&housetype=&page=1")
