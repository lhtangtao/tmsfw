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
        sql_script = 'CREATE TABLE new_house' + current_data + ' (Id varchar(30),current_data varchar(30),location varchar(30),village varchar(30),house_type varchar(30),square varchar(30),orientation varchar(30), decorate varchar(30),money varchar(30),per_square VARCHAR (30),url varchar(300),page varchar(30))'
        cur.execute(sql_script)
        sql_script = "ALTER TABLE `test`.`houseinfo" + current_data + "` MODIFY COLUMN `Id` int(30) NOT NULL FIRST,MODIFY COLUMN `square` int(30) NULL DEFAULT NULL AFTER `house_type`,MODIFY COLUMN `money` int(30) NULL DEFAULT NULL AFTER `decorate`,MODIFY COLUMN `per_square` int(30) NULL DEFAULT NULL AFTER `money`,MODIFY COLUMN `page` int(30) NULL DEFAULT NULL AFTER `url`,ADD PRIMARY KEY (`Id`);"
        cur.execute(sql_script)
        x = True
    except Exception as e:
        x = False
        print e
        sql_script = "truncate table houseinfo" + current_data
        cur.execute(sql_script)
    cur.close()
    conn.commit()
    conn.close()
    return x
