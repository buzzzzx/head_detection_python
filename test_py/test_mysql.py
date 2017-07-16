#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-20 16:27:34
# @Author  : buzz (buzzzzx233@gmail.com or zhuxin_dev@qq.com)
# @Link    : ${link}
# @Version : $Id$

import pymysql

conn = pymysql.connect(host='192.168.253.12', port=3306,
                       user='root', passwd='123456', db='head')
cur = conn.cursor()

# insert
data_one = cur.execute(
    'insert into head_count(people_count, date, time) values(%s, %s)', ())
conn.commit()
# 关闭指针对象
cur.close()
# 关闭连接对象
conn.close()
# 打印结果
print(data_one)