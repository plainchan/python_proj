#!/usr/bin/env python3
from functools import reduce


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def test():
    v = map(str,[x for x in range(10)])   #0-9转换成字符串,返回的是迭代器
    print(list(v))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算。返回的是一个计算的最终结果
# 左边的参数 x 是累积值,而右边的参数 y 则是来自 sequence 的更新值。
# 返回的值
def test1():
    v = reduce(lambda x,y:x+y,[n for n in range(1,11)])
    print(v)

# filter()也接收一个函数和一个序列。从一个序列中筛出符合条件的元素。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def test2():
    v = filter(lambda x:x>0,[n for n in range(-5,10)])
    print(list(v))
    
# sorted(iterable, *, key=None, reverse=False)
#iterable – 可迭代对象。
# key – 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse – 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
def test3():
    v = sorted(lambda x,y:x>y,[n for n in range(10)])
    print(list(v))

if __name__ == "__main__":
    test3()