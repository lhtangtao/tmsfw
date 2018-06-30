#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=tmsfw 
#author=lhtangtao
#time=2018/6/6 15:14
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=数据库相关操作
"""

import time
import pymysql

time.localtime(time.time())
current_data = time.strftime('%Y%m%d', time.localtime(time.time()))


def init_db():
    """
    请在此处输入数据库的信息
    :return:
    # """
    # connect = MySQLdb.connect(
    connect = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        db='tmsfw',
        charset="utf8",  # 确保没有乱码
        passwd='root'
    )
    assert isinstance(connect, object)
    return connect


def create_table():
    """
    创建一张表，如果这个表存在的话则跳过 必须要确保数据库名字为test且存在
    :return: 如果存在 返回False，如果不存在则会建立一张表并且返回true
    """
    conn = init_db()
    cur = conn.cursor()
    try:
        sql_script = 'CREATE TABLE new_house' + current_data + " (`ID` integer(10) NOT NULL AUTO_INCREMENT COMMENT '唯一主键', `location` varchar(300) CHARACTER SET ascii NOT NULL DEFAULT '' COMMENT '所在行政区域',  `village` varchar(30) NOT NULL DEFAULT '' COMMENT '小区名字', `other_name` varchar(30) NULL DEFAULT '' COMMENT '小区别名',`building` varchar(30) NULL DEFAULT '' COMMENT '楼栋', `room` varchar(30) NULL COMMENT '房号',`area` double NULL COMMENT '建筑面积', `inner_area` double NULL COMMENT '套内面积',`rate` double NULL COMMENT '得房率',  `billet_unit_price` double NULL COMMENT '毛坯单价',  `decoration_price` double NULL COMMENT '装修价',  `total_price` double NULL COMMENT '总价',  `operation` varchar(30) NULL COMMENT '操作', `url_address` varchar(100) NULL COMMENT '具体链接',  PRIMARY KEY (`ID`)) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;"
        cur.execute(sql_script)
        sql_script = 'ALTER TABLE new_house' + current_data + " MODIFY COLUMN `location` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '所在行政区域' AFTER `ID`;"
        # print sql_script
        cur.execute(sql_script)
        x = True
    except Exception as e:
        x = False
        sql_script = "truncate table new_house" + current_data
        cur.execute(sql_script)
    cur.close()
    conn.commit()
    conn.close()
    return x


def insert_info(kind, value):
    """
    要插入的数据列名和数值
    :param kind:
    :param value:
    :return:
    """
    conn = init_db()
    cur = conn.cursor()
    try:
        sql_script0 = "INSERT INTO new_house%s" % current_data
        sql_script1 = "(%s) VALUES " % kind
        sql_script2 = "('%s')" % value
        sql_script = sql_script0 + sql_script1 + sql_script2
        # print sql_script
        cur.execute(sql_script)
        x = True
    except Exception as e:
        x = False
        print e
        print(sql_script)
    cur.close()
    conn.commit()
    conn.close()
    return x


def update_info(kind, value, id_num):
    conn = init_db()
    cur = conn.cursor()
    try:
        sql_script0 = "UPDATE new_house%s SET" % current_data
        sql_script1 = " %s =" % kind
        sql_script2 = "('%s')" % value
        sql_script3 = "where id='%s'" % id_num
        sql_script = sql_script0 + sql_script1 + sql_script2 + sql_script3
        cur.execute(sql_script)
        x = True
    except Exception as e:
        x = False
        print e
        print(sql_script)
    cur.close()
    conn.commit()
    conn.close()
    return sql_script


if __name__ == '__main__':
    create_table()
    # insert_info("ID", 1)
