---
layout: post
title:  python 高阶
date:   2019-03-06
categories: Python
---

<!-- MarkdownTOC -->




## python 高阶

### 条件表达式：
> y = 33 if x>0 else 55
> return men if gender else women

### 列表推导式

> [i for i in range(1000) if i%2==0]

### map()函数

 (1) map(函数名，sequence)

 (2) 可用于数据清洗

 (3) map func类型，可以用list(map())转换
### 匿名函数 lamba

> lambda arguments: expression

* This function can have any number of arguments but only one expression, which is evaluated and returned.
* One is free to use lambda functions wherever function objects are required.
* You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
* It has various uses in particular fields of programming besides other types of expressions in functions.


> list_a = [lambda a: a**3, lambda b: b**3]
>list_a[0]-------<function <lambda> at 0x0259B8B0>
> g = list_a[0]
>g(2)---------8

```
#lambda结合map
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
result = map(lambda x, y: x * 2 + y, l1, l2)
print(list(result))
```
> [4, 10, 16, 22, 28]


### 深拷贝、浅拷贝

浅拷贝只复制指向某个对象的指针，而不复制对象本身，新旧对象还是共享同一块内存。但深拷贝会另外创造一个一模一样的对象，新对象跟原对象不共享内存，修改新对象不会改到原对象。

![深、浅拷贝](https://s1.ax1x.com/2020/03/31/GKkEE6.png)


### 多进程

```python
import os
import time
from datetime import datetime
from multiprocessing import Process

def run_proc(n):
    print('第{}次循环，子进程id:{}，父进程id:{}'.format(n, os.getpid(), os.getppid()))
    time.sleep(1)
start = datetime.now()
# 2. 多进程并行执行

# 2.1 多进程异步并行执行，进程间没有先后顺序
for i in range(10):
    p = Process(target=run_proc, args=(i,))
    p.start()
print('耗时:', datetime.now() - start)

# 2.2 多进程同步并行执行，进程间有先后顺序
start = datetime.now()
for i in range(10):
    p = Process(target=run_proc, args=(i,))
    p.start()
    p.join()
print('耗时:', datetime.now() - start)
```
#### 进程池
```python
from multiprocessing import Pool
import os
import time
import random
 
def worker(msg):
	t_start=time.time() #记录从1970.0.0到现在的秒数
	print("%s 开始执行，进程号为%d"%(msg,os.getpid()))
	#random.random()随机生成0~1之间的浮点数
	time.sleep(random.random()*2)
	t_stop=time.time()
	print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))
 
def main1():
	po=Pool(3) #定义一个进程池，最大进程数3
	for i in range(0,10):
		po.apply(worker,(i,))#等待上一次任务完成之后再次添加新的任务，堵塞式添加
	
	print("---start---")
	po.close()#关闭进程池，关闭后po不再接受新的请求
	po.join()#等待po中所有子进程执行完成，必须放在close后
	print("-----------end----------")


def main2():
	po=Pool(3) #定义一个进程池，最大进程数3
	for i in range(0,10):
		po.apply_async(worker,(i,))
	print("---start---")
	po.close()#关闭进程池，关闭后po不再接受新的请求
	po.join()#等待po中所有子进程执行完成，必须放在close后
	print("-----------end----------")

```

### yield 生成器

生成器表达式的标准方式是以圆括号的形式，括号内可以是一个列表推导式。
> generator_expression ::= "(" expression comp_for ")"

生成器表达式生语法和列表推导式相同，列表推导式是以大括号的形式存在。列表推导式是直接创建一个列表，但是由于受到内存的限制，列表的容量有上限，而生成器则不需要一下子创建完整的列表，而是一边循环一边计算。
生成器表达式生成了一个生成器对象，但其中的变量是以延迟方式获取，直到调用生成器的__next__()方法

```python
ge = (2 * i for i in range(3))
print(next(ge))  # 输出：0
print(next(ge))  # 2
print(next(ge))  # 4
print(next(ge))  # StopIteration

```
### Python中常用内建方法

1. __repr__如果用IDE软件操作，功能与__str__完全一样，都是实例可视化显示
2. 开发中如果用户需要可视化实例内容，只需要重写__str__或者__repr__方法之一即可。如果两个都有的话，默认调用__str__.
3. 两者的区别就是使用命令行操作：
 3.1 __str__重写后，如果直接实例stu回车的话话，显示的是stu实例在内存中的地址，跟print(stu)不一样。
 3.2 __repr__重写后，如果直接实例stu回车的话，效果跟使用print(stu)一样，返回内容，不是内存地址。 
 
 
 ### 


