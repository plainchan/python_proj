#!/usr/bin/env python3

#*args,args中保存的是没有利用的所有多余参数，保存方式为元组
def test(*args):
    print(*args)



if __name__ == "__main__":
    test(1,2,3,4,5,6,7)