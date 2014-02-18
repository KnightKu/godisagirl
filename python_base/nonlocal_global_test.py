#!/usr/bin/env python3

#global 声明使用全局变量
#nonlocal 声明使用外围变量(非全局变量)，例如:上层函数变量等

#-*-coding:utf-8-*-
spam = None
def scope_test():
    def do_local():
        spam = 'local spam'
   
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
       
    def do_global():
        global spam
        spam = 'global spam'
        print (spam) #此处输出的是全局变量spam的值
       
    spam = 'test spam'
    do_local()
    print('after local assignment:',spam)
   
    do_nonlocal()
    print('after nonlocal assignment:',spam)
   
    do_global()
   
    #这里的作用域是scope_test函数，即spam是局部的
    #和do_global函数中的spam不同
    print('after global assignment:',spam)


#global
gcount = 0

def global_test():
    print (gcount)
    
def global_counter():
    global gcount
    gcount +=1
    return gcount
    
def global_counter_test():
    print(global_counter())
    print(global_counter())
    print(global_counter())

#nonlocal
#nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
    
def make_counter_test():
  mc = make_counter()
  print(mc())
  print(mc())
  print(mc())
if '__main__' == __name__:
    scope_test()
    print (spam)
