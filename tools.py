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


def get_administrative_location(location_verbose):
    if u"上城" in location_verbose:
        administrative = u"上城"
    elif u"下城" in location_verbose:
        administrative = u"下城"
    elif u"之江" in location_verbose or u"西湖" in location_verbose:
        administrative = u"西湖"
    elif u"东湖街道" in location_verbose or u"中泰街道" in location_verbose or u"临平街道" in location_verbose or u"乔司街道" in location_verbose or u"五常街道" in location_verbose or u"仁和街道" in location_verbose or u"仓前街道" in location_verbose or u"余杭经济开发区" in location_verbose or u"余杭街道 " in location_verbose or u"南苑街道" in location_verbose or u"塘栖镇" in location_verbose or u"崇贤街道" in location_verbose or u"径山镇" in location_verbose or u"星桥街道" in location_verbose or u"瓶窑镇" in location_verbose or u"良渚街道" in location_verbose or u"运河街道" in location_verbose or u'钱江经济开发区' in location_verbose or u"闲林街道" in location_verbose or u"鸬鸟镇" in location_verbose:
        administrative = u"余杭"
    elif u"下沙" in location_verbose or u"江干" in location_verbose:
        administrative = u"江干"
    elif u"临浦街道" in location_verbose or u"义桥镇" in location_verbose or u"义蓬街道" in location_verbose or u'党湾镇' in location_verbose or u"北干街道" in location_verbose or u"城厢街道" in location_verbose or u"宁围街道" in location_verbose or u"所前镇" in location_verbose or u"新塘街道" in location_verbose or u"新湾街道" in location_verbose or u"新街街道" in location_verbose or u"河庄街道" in location_verbose or u"瓜沥镇" in location_verbose or u"萧山区" in location_verbose or u"萧山经济技术开发区" in location_verbose or u"蜀山街道" in location_verbose or u"衙前镇" in location_verbose or u"闻堰街道" in location_verbose or u"靖江街道" in location_verbose:
        administrative = u"萧山"
    elif u"拱墅" in location_verbose:
        administrative = u"拱墅"
    elif u"滨江" in location_verbose:
        administrative = u"滨江"
    else:
        administrative = u"未知区域"
    return administrative


if __name__ == '__main__':
    print get_administrative_location(u"[西湖]星桥街道临丁路以北，学堂港以西")
