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
from sql import create_table, update_info
from tools import get_administrative_location
from village import get_village_page_num, get_village_info

if __name__ == '__main__':
    id_num = 1
    id_num_source = 0
    create_table()  # 创建一张数据库 把数据往里面写
    new_house_page = int(get_page_num())  # 查看http://www.tmsf.com/newhouse/property_searchall.htm 这个网站 一共有多少页新房。
    print u"一共有"+str(new_house_page)+u"页新房小区"
    # 修改page=
    # http://www.tmsf.com/newhouse/property_searchall.htm?searchkeyword=&keyword=&sid=&districtid=&areaid=&dealprice=&propertystate=&propertytype=&ordertype=&priceorder=&openorder=&view720data=&page=3&bbs=&avanumorder=&comnumorder=
    # 随后获取每页的小区的url链接地址
    url1 = "http://www.tmsf.com/newhouse/property_searchall.htm?searchkeyword=&keyword=&sid=&districtid=&areaid" \
           "=&dealprice=&propertystate=&propertytype=&ordertype=&priceorder=&openorder=&view720data=&page="
    url2 = "&bbs=&avanumorder=&comnumorder="
    # 示例网址：http://www.tmsf.com/newhouse/property_33_514158189_price.htm
    now_time_start = datetime.datetime.now()  # 现在
    for i in range(1, new_house_page + 1):
        now_time_start_page = datetime.datetime.now()  # 现在
        url = url1 + str(i) + url2
        every_page_village_url_list = get_village_href(url)  # 返回一维数组 里面是每个小区局的一房一价网页地址
        every_village_location_verbose = get_location(url)  # 返回一维数组 里面是每个小区所在的位置
        page_house_num = len(every_page_village_url_list)  # 这个页面里的小区数量，一般而言这个数字是6
        for x in range(0, page_house_num):
            now_time_start_village = datetime.datetime.now()  # 现在
            print str(now_time_start_village)+u"现在开始执行爬虫的小区地址是："+every_page_village_url_list[x]  # 示例 http://www.tmsf.com/newhouse/property_330184_430659766_price.htm
            try:
                id_num_source=id_num
                village_page_num = int(get_village_page_num(every_page_village_url_list[x]))  # 获取每个小区有多少房产信息的页面
                print u"这个小区有"+str(village_page_num)+ u"页房产信息"
                for y in range(1, village_page_num + 1):
                    url_village = every_page_village_url_list[
                                      x] + "?isopen=&presellid=&buildingid=&area=&allprice=&housestate=&housetype=&page=" + str(
                        y)
                    print u"现在开始采集该网页的数据："+url_village +u'开始获取信息的id_num = '+str( id_num)
                    id_num = get_village_info(url_village, id_num,
                                              every_village_location_verbose[x]
                                              , get_administrative_location(every_village_location_verbose[x]))  # 一般会写14条数据 id会自增14
                    print u"现在跑到了第"+ str(id_num)+u"条数据" +u"该小区的第"+str(y)+u"页  " +u'结束获取信息的id_num = '+str( id_num)
            except:
                print u'这个页面不是典型的一房一价页面，它的地址需要手动获取，地址是：' + every_page_village_url_list[x]
            now_time_end_village = datetime.datetime.now()  # 现在
            print u"爬完这个小区耗时为："+str(now_time_end_village - now_time_start_village)
            print u"现在爬到了 第"+str(id_num)+u"条数据，新增"+str(id_num-id_num_source) + u" 在该小区的第"+str(x) +u"页"
        now_time_end = datetime.datetime.now()  # 现在
        print u'刚刚爬虫完毕的是第' + str(i) + u'页的所有新房信息，他的地址是' + url+u"花费的时间为："+str(now_time_end - now_time_start_page)  # 计算时间差
    now_time_end = datetime.datetime.now()  # 现在
    print u"爬虫完成，全部耗时如下："
    print (now_time_end - now_time_start)  # 计算时间差
