---
layout: post
title:  python 高阶
date:   2019-03-06
categories: Python
---

<!-- MarkdownTOC -->




## python 高阶

### 条件表达式：
> if x>0 else float("nan")

### 列表推导式

> [i for i in range(1000) if i%2==0]

### map()函数

（1）map(函数名，sequence)

（2）可用于数据清洗

### 匿名函数 lamba

（1）简单的函数操作

（2）返回值是func类型

（3）可结合map()完成数据清洗


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

#### 

