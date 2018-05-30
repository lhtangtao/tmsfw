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
