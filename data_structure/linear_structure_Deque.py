#-*- coding:utf-8 -*-
#Author:李明洲
#@Time:2020/6/3 10:20
#-*- coding: UTF-8 -*-

#双向队列

import time
from collections import deque


#  可以指定 队列的长度
mydeque=deque(maxlen=10)
print(mydeque.maxlen)

# 默认从右边加入
mydeque.append(10)
mydeque.append(12)
print(mydeque)

# time.sleep(4)
# 也可以从左边加入
mydeque.appendleft('a')
mydeque.appendleft('b')
mydeque.appendleft('c')
mydeque.appendleft('d')
mydeque.appendleft('e')
print(mydeque)

mylist= range(5,8)
# 也可以加入一个列表，默认从右边加入
# mydeque.extend(mylist)
mydeque.extendleft(mylist)
print(mydeque)

# 出队列,返回出队列的元素
# 可以从左边也可以从右边 出队列
mydeque.pop()
mydeque.popleft()

# 查看 队列里面元素个数
print(len(mydeque))

# 统计元素的个数
#统计a 有几个
print(mydeque.count('a'))


# 在某个位置insert 一个元素
# insert(i, x)
# Insert x into the deque at position i.
d1=deque([10, 12, 13, 14])
d1.insert(2,'frank')
print(d1)

#翻转操作
# deque.reverse()
print(mydeque)
mydeque.reverse()
print(mydeque)

# remove 移除某个元素
print(mydeque)
mydeque.remove(10)
print(mydeque)

# 清空队列元素 clear
print(mydeque)
mydeque.clear()
print(mydeque)

# copy 浅拷贝
# Create a shallow copy of the deque.
l1 = [6, 5, 8, 3, 9, 0, 2, 7, 4, 1]
d3 = deque(l1)
print(d3)
d4 = d3.copy()
print(d4)
