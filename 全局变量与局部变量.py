#!/usr/bin/env python3


#全局变量在整个py文件中声明，全局范围内可以使用
#在函数内部，如果局部变量与全局变量变量名一样，则优先调用局部变量。
#如果想在函数内部改变全局变量，需要在前面加上global关键字
value = 100
def test():
    value = 250     #与全局变量同名,不是修改全局变量,而是创建局部变量
    print(value)
    
def test1():
    global value
    value = 1000    #修改的是全局变量
    print(value)
  

#函数内创建全局变量,在变量名前面加上global
def test2():
    global num
    num = 123
    print(num)
    
#回调函数中创建的局部变量,要想下次回调继续使用,要声明为全局变量



if __name__ == "__main__":
    test()
    test1()            #函数体内修改全局变量
    test2()            #函数体内创建全局变量
    print(num)  

