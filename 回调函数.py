#!/usr/bin/env python3
import time


#定义一个函数，然后将这个函数的函数名传递给另一个函数做参数，以这个参数命名的函数就是回调函数。


####回调函数
def add(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
        


def calcSum(num,add):
    print(add(num))


#######
def my_callbcak(args):
    print(*args)

def caller(args, func):
    func(args)




if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    calcSum(nums,sum)
    caller((1,2), my_callbcak)
