#!usr/bin/python3

# a = input("输入名字")
# print(a)

# print("{},{}".format("a",1))
# print("i am {},the {}".format("ly",1))
# print("{:.3f}".format(10.6789))
'''
print("{:b}".format(155))
print("{:x}".format(155))
print("{:8}:{:8}".format(10,20))
print("{:<8}:{:>8}".format(10,20))
print("*"*20)
'''

"""
name = "Tom"
role = "mine"
print(name,"is",role)

a = b = c = "hiddleston"
print(a)
"""
"""
print("{:.2f}".format(-1.23456789))
print("{:+.2f}".format(-1.23456789))
print("{:.0f}".format(-1.23456789))
print("{:0>3d}".format(11))
print("{:x<5d}".format(444))
print("{:,}".format(10000))
print("{:,}".format(100))
print("{:10d}".format(222))
print("{:<10d}".format(333))
"""

print("{2}{0}{1}".format(".","Holland","Tom"))
print("i don't {what}".format(what="understand"))

finish = {"first":"finally","second":"done"}
print("{first} {second}".format(**finish))

