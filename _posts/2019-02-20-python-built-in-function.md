---
layout:     post
title:      内置函数Python
date:       2019-2-20
author:     Louis
catalog:    Python

---
<!-- MarkdownTOC -->




# 内置函数

## **1. repr()函数**

### 语法

repr(object)
参数
object -- 对象。
返回一个对象的 string 格式。

### 实例

```
s = 'RUNOOB'
repr(s)
>>> "'RUNOOB'"
dict = {'runoob': 'runoob.com', 'google': 'google.com'};
repr(dict)
>>> "{'google': 'google.com', 'runoob': 'runoob.com'}"
```
## **2. isinstance()函数**
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
```
isinstance() 与 type() 区别：

type() 不会认为子类是一种父类类型，不考虑继承关系。

isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
```
### 语法
isinstance(object, classinfo)

**参数**
 - object -- 实例对象。
 - classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
 
**返回值**

如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。

### 实例

```
>>>a = 2
>>> isinstance (a,int)
True
>>> isinstance (a,str)
False
>>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
True
```

### type() 与 isinstance()区别：
```
class A:
    pass 
class B(A):
    pass
isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
```