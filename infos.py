#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=tmsfw 
#author=lhtangtao
#time=2018/6/5 23:02
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=房产info信息
"""


class Info(object):
    """
    房产信息类
    """

    def __init__(self):
        self.building = None
        self.room_number = None
        self.covered_area = None
        self.inner_area = None
        self.housing_rate = None
        self.billet_unit_price = None
        self.decoration_price = None
        self.total_price = None
        self.operation = None

    def set_building(self, building):
        self.building = building

    def set_room_number(self, room_number):
        self.room_number = room_number

    def set_covered_area(self, covered_area):
        self.covered_area = covered_area

    def set_inner_area(self, inner_area):
        self.inner_area = inner_area

    def set_housing_rate(self, housing_rate):
        self.housing_rate = housing_rate

    def set_billet_unit_price(self, billet_unit_price):
        self.billet_unit_price = billet_unit_price

    def set_decoration_price(self, decoration_price):
        self.decoration_price = decoration_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    def set_operation(self, operation):
        self.operation = operation
