#!/usr/bin/env python
# encoding: utf-8
'''
@author: liyao
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file: chapter_02.py
'''
'''
a=2
b=10
c=7
y=3
yy=4
z=5
zz=6
x=8
xx=9
xxx=0
print(a+b,b-c,a*b,b/c,b%c,c**a,b//c)
print(a==b,a!=b,a>b,a<b,a>=b,a<=b)

y+=a
yy-=a
z*=a
zz/=a
x%=a
xx**=a
xxx//=a
print(y,yy,z,zz,x,xx,xxx)

print(a and b,a or b,not a)
'''
'''
a=30
b=17
print("{:b}".format(a),"{:b}".format(b))
print("{:b}".format(a&b),"{:b}".format(a|b),"{:b}".format(a^b),"{:b}".format(~b),"{:b}".format(a<<3),"{:b}".format(b>>2))
'''

'''
a="this is a string "
print(a[3:7])

b=True
print(b+3)
del b
print(b+5)

print(a*2)
print(a+"!")
print("\""+a+"\"")
print("\r\r")
# 没明白不让反斜杠转义意义在哪。。。。
'''

'''
a=[1,2,"b","hhh"]
print(a[1:3])
b=[3,"xxx","2"]
print(a+b)
c=(6,"yy")
a[0]=5
print(a)
c[0]=5
print(c)
'''

'''
a={"u","r","s"}
b=set()
print(a&b)
# 没明白set()函数定义集合啥情况。。。

c={"name":"LY","gender":"F"}
print(c)
c["hobby"]="m"
print(c)
'''

'''
c={"name":"LY","gender":"F"}
print(c)
print(int("33",8),float("4"),complex(1,2),str(c),repr("aa"))

sss=[("a","b"),("c","d")]
print(sss)
uu=dict(sss)
print(dict(sss),uu)
print(uu["a"])
'''

'''
b="Tom"
a=input()
# 默认输入的为字符串。。。。
if a==b:
    print("Yes")
elif int(a)==1:
    print("ah")
else:
    print("No")
'''
'''
a=input()
b=int(a)
while b<10:
    if b==1:
        break
    else:
        print(b)
        b+=1
else:
    print("done")
'''

for i in range(1,10):
        for j in range(i,10):
            print(j,"*",i,"=",i*j," ",end="")
            if j==9:
                print(end="\n")