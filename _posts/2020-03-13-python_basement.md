---
layout: post
title:  python 基础知识
date:   2019-03-06
categories: Python
---

<!-- MarkdownTOC -->




## 输入输出

```python
import sys
try:
    while True:
        print('Please input a number:')
        n = int(sys.stdin.readline().strip('\n')) #strip('\n')表示以\n分隔，否则输出是“字符串+\n”的形式
        print('Please input some numbers:')
        sn = sys.stdin.readline().strip()#若是多输入，strip()默认是以空格分隔，返回一个字符串。
        if sn == '':
            break
        sn = map(int,sn.split()) #.split()默认以空格分离，输出list
        print(n)
        print(sn,'\n')
except:
    pass
```
![测试](https://s1.ax1x.com/2020/03/13/8nIYTI.png)

## 格式化输出
```python
#使用'{}'占位符
print('I\'m {},{}'.format('hello','Welcome to my space!'))
```
> I'm hello,Welcome to my space!
```
#也可以使用'{0}','{1}'形式的占位符
print('{0},I\'m {1},my E-mail is {2}'.format('Hello','spach','spach@163.com'))
#可以改变占位符的位置
print('{1},I\'m {0},my E-mail is {2}'.format('spach','Hello','spach@163.com'))
``` 
> Hello,I'm spach,my E-mail is spach@163.com
> Hello,I'm spach,my E-mail is spach@163.com

> print('#' * 40)
> ########################################

```python
#使用'{name}'形式的占位符
print('Hi,{name},{message}'.format(name = 'Tom',message = 'How old are you?'))
```
> Hi,Tom,How old are you?
 
```python
#混合使用'{0}','{name}'形式
print('{0},I\'m {1},{message}'.format('Hello','spach',message = 'This is a test message!'))
``` 
> Hello,I'm spach,This is a test message!

###下面进行格式控制

```python
import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
```
> The value of PI is approximately 3.141592653589793.

> The value of PI is approximately 3.141592653589793.

> The value of PI is approximately 3.142.

这里的!r和%r类似，但是!r只用于format形式输出

> b = 'hello, %r' % 123#可以

> b = 'hello, !r' % 123 #会报错



```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
``` 
Sjoerd     ==>       4127

Jack       ==>       4098

Dcab       ==>       7678
 
```python
print("{:.2f}".format(3.1415926)) #3.14,保留小数点后两位
print("{:+.2f}".format(3.1415926)) #+3.14 带符号保留小数点后两位
print("{:+.2f}".format(-10)) #-10.00 带符号保留小数点后两位
print("{:+.0f}".format(-10.00)) #-10  不带小数
print("{:0>2d}".format(1))  #01 数字补零 (填充左边, 宽度为2)
print("{:x<2d}".format(1)) #1x 数字补x (填充右边, 宽度为4)
print("{:x<4d}".format(10))  #10xx 数字补x (填充右边, 宽度为4)
print("{:,}".format(1000000)) #1,000,000 以逗号分隔的数字格式
print("{:.2%}".format(0.12))  #12.00% 百分比格式
print("{:.2e}".format(1000000))  #1.00e+06 指数记法
print("{:<10d}".format(10))  #10 左对齐 (宽度为10)
print("{:>10d}".format(10))  #        10 右对齐 (默认, 宽度为10)
print("{:^10d}".format(10))  #    10 中间对齐 (宽度为10)
```

字典输出：
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
```
> Jack: 4098; Sjoerd: 4127; Dcab: 8637678


```python
tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"   # {1:{3}^10} 1表示位置，{3}表示用第3个参数来填充，^表示居中，10表示占10个位置
print(tplt.format("排名","学校名称","总分",'*'))
```
```python
args = ['zdd', ',']
kwargs = {'obj': 'world', 'name': 'python'}
print('hello {obj} {} i am {name}'.format(*args, **kwargs))
```
> out: hello world zdd i am python


两种输入形式：

(1) sys.stdin.readline() 标准读入输入的一行，包含"\n"

(2) input.readline() 标准读入输入的一行，不包含"\n"

## 字典操作

(1)对可迭代的tuple变字典

> dict([(1,5),(2,9)])
> {1: 5, 2: 9}

> dict3 = dist{"name": "Tom", "job": "waiter"}

增加键值对：

```python
print('方案一 list作为dict的值 值允许重复')
dict1= {}
key = "name"
value1 = "Alice"
dict1.setdefault(key, []).append(value1)
value2 = "Alice"
dict1.setdefault(key, []).append(value2)
``` 

> result : dict1 = {'name': ['Alice', 'Alice']}

```python
print('方案二 使用子字典作为dict的值 值不允许重复')
dict2 = {}
key = "school"
keyin = "grade"
value = "one"
dict2.setdefault(key, {})[keyin] = value
keyin = "class"
value = "two"
dict2.setdefault(key, {})[keyin] = value
keyin = "sex"
value = "male"
dict2.setdefault(key, {})[keyin] = value
```
    
> dict2 = {'school': {'grade': 'one', 'class': 'two', 'sex': 'male'}}

```python
print('方案三 使用set作为dict的值 值不允许重复')
dict3 = {}
key = "name"
value = "Alice"
dict3.setdefault(key, set()).add(value)
value = "Alice"
dict3.setdefault(key, set()).add(value)
value = "Louis"
dict3.setdefault(key, set()).add(value)
print(dict3)
```

> dict3 = {'name': {'Alice', 'Louis'}}

```python
file = "wenjian"
dist = {file : "1.txt"}
value = "2.txt"
if file in dist:#有此键
    dist.setdefault(file, []).append(value) #dist.setdefault(file, set).add(value)
else:
    dist.setdefault(file, []).append(value) #dist.setdefault(file, set).add(value)
```

> 注意set和[]区别，上下需要同步.或者可以使用dist.get(file).append(value),但这个需要在初始化时将file的value转化为list
如：dist[file] = [value]

## list之排序

> list1 = [as, ds, ew, gw, qi, cv, nf, re]

> list1.sort() #以首字母排序（默认升序） 

> list1.sort(reverse=True) #以首字母排序（默认升序）

> list1.sort(key=lambda x:x[-1])


## json file

## 阿拉伯数字转换成中文大写

```python
def num_to_char(num):
    """数字转中文"""
    num=str(num)
    new_str=""
    num_dict={"0":u"零","1":u"一","2":u"二","3":u"三","4":u"四","5":u"五","6":u"六","7":u"七","8":u"八","9":u"九"}
    listnum=list(num)
    shu=[]
    for i in listnum:
        shu.append(num_dict[i])
    new_str="".join(shu)#list->str
    return new_str
 
```

## zip函数

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
zip([iterable, ...])
```python
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
```