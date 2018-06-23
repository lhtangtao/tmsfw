#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=tmsfw 
#author=lhtangtao
#time=2018/6/23 16:58
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=主页
"""
import datetime
import time

from main_page import get_page_num, get_village_href, get_location
from sql import create_table
from village import get_village_page_num

if __name__ == '__main__':
    create_table()  # 创建一张数据库 把数据往里面写
    new_house_page = int(get_page_num())  # 查看http://www.tmsf.com/newhouse/property_searchall.htm 这个网站 一共有多少页新房。
    # 修改page=
    # http://www.tmsf.com/newhouse/property_searchall.htm?searchkeyword=&keyword=&sid=&districtid=&areaid=&dealprice=&propertystate=&propertytype=&ordertype=&priceorder=&openorder=&view720data=&page=3&bbs=&avanumorder=&comnumorder=
    # 随后获取每页的小区的url链接地址
    url1 = "http://www.tmsf.com/newhouse/property_searchall.htm?searchkeyword=&keyword=&sid=&districtid=&areaid" \
           "=&dealprice=&propertystate=&propertytype=&ordertype=&priceorder=&openorder=&view720data=&page="
    url2 = "&bbs=&avanumorder=&comnumorder="
    # 示例网址：http://www.tmsf.com/newhouse/property_33_514158189_price.htm
    now_time_start = datetime.datetime.now()  # 现在

    now_time_end = datetime.datetime.now()  # 现在
    print (now_time_end - now_time_start)  # 计算时间差
    for i in range(1, 2 + 1):
        url = url1 + str(i) + url2
        every_page_village_url_list = get_village_href(url)  # 返回一维数组 里面是每个小区局的一房一价网页地址
        every_village_location_verbose = get_location(url)  # 返回一维数组 里面是每个小区所在的位置

        page_house_num = len(every_page_village_url_list)  # 这个页面里的小区数量，一般而言这个数字是6
        for x in range(0, page_house_num):
            print every_page_village_url_list[x] # 示例 http://www.tmsf.com/newhouse/property_330184_430659766_price.htm
            village_page_num = int(get_village_page_num(every_page_village_url_list[x]))  # 获取每个小区有多少房产信息的页面
            url_village1="http://www.tmsf.com/newhouse/property_330181_439549419_price.htm?isopen=&presellid=&buildingid=&area=&allprice=&housestate=&housetype=&page="+ str(x)
            # for x in range(1,village_page_num):

        # TODO  对这一维数组进行操作，这个一维数组里的都是
