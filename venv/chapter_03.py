#!/usr/bin/env python
# encoding: utf-8
'''
@author: liyao
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file: chapter_03.py
@time: 2018/11/21 9:44
'''
import sys

stu_uni = []
def stu_mg():
    print('='*10,' 学员管理系统 ','='*10)
    print('1. 查看学员信息       2. 添加学员信息')
    print('3. 删除学员信息       4. 退出系统')
    print('=' * 28)
    op=input('请输入对应的选择：')
    if int(op)==1:
        ch1()
    elif int(op)==2:
        ch2()
    elif int(op)==3:
        ch3()
    elif int(op)==4:
        ch4()
    else:
        print('无效选择，回车返回：')
        stu_mg()

def ch1():
    if len(stu_uni)==0:
        print('还未录入学员，请返回上一级进行添加:')
        stu_mg()
    else:
        print('{:^45}'.format('学员信息查询'))
        print('|', '{:^9}'.format('sid'), '|','{:^9}'.format('name'), '|', '{:^9}'.format('gender'), '|', '{:^9}'.format('age'), '|', '{:^9}'.format('class'), '|')
        for stu in stu_uni:
            print('|','{:^9}'.format(stu[0]),'|','{:^9}'.format(stu[1]),'|','{:^9}'.format(stu[2]),'|','{:^9}'.format(stu[3]),'|','{:^9}'.format(stu[4]),'|')
        print('=' * 45)
        stu_mg()

def ch2():
    s = len(stu_uni)+1
    nm = input('请输入名字：')
    gd = input('请输入性别：')
    ag = input('请输入年龄：')
    cls = input('请输入班级：')
    stu_new = [s, nm, gd, ag, cls]
    stu_uni.append(stu_new)
    print('添加学员信息成功，按回车键继续！')
    stu_mg()

def ch3():
    print('{:^45}'.format('学员信息删除'))
    print('|', '{:^9}'.format('sid'), '|', '{:^9}'.format('name'), '|', '{:^9}'.format('gender'), '|',
          '{:^9}'.format('age'), '|', '{:^9}'.format('class'), '|')
    for stu in stu_uni:
        print('|', '{:^9}'.format(stu[0]), '|', '{:^9}'.format(stu[1]), '|', '{:^9}'.format(stu[2]), '|',
              '{:^9}'.format(stu[3]), '|', '{:^9}'.format(stu[4]), '|')

    d=input('请输入需要删除的学员sid：')
    for stu2 in stu_uni:
        while int(d) in stu2:
            indx=stu_uni.index(stu2)
            break
    stu_uni.pop(indx)
    print('学员信息删除成功')
    print('|', '{:^9}'.format('sid'), '|', '{:^9}'.format('name'), '|', '{:^9}'.format('gender'), '|',
          '{:^9}'.format('age'), '|', '{:^9}'.format('class'), '|')
    for stu3 in stu_uni:
        print('|', '{:^9}'.format(stu[0]), '|', '{:^9}'.format(stu[1]), '|', '{:^9}'.format(stu[2]), '|',
              '{:^9}'.format(stu[3]), '|', '{:^9}'.format(stu[4]), '|')
    print('=' * 28)
    stu_mg()

def ch4():
    print('再见')
    sys.exit()

def main():
    stu_mg()

if __name__ == '__main__':
    main()