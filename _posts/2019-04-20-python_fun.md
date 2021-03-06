---
layout: post
title: python函数
date:   2019-04-20
categories: python
---

<!-- MarkdownTOC -->




# python函数
## zip函数
### 描述
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
### 语法
zip([iterable, ...])
参数说明：
- iterabl -- 一个或多个迭代器;
# 返回值
返回元组列表
# 实例
 
```

    a = [1,2,3]
    b = [4,5,6]
    c = [4,5,6,7,8]
    zipped = zip(a,b)     # 打包为元组的列表
    >>> [(1, 4), (2, 5), (3, 6)]
    zip(a,c)              # 元素个数与最短的列表一致
    >>> [(1, 4), (2, 5), (3, 6)]
    zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    >>> [(1, 2, 3), (4, 5, 6)]

```

## enumerate() 函数
### 描述
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
### 语法
enumerate(sequence, [start=0])
参数说明：
- sequence -- 一个序列、迭代器或其他支持迭代对象
- start -- 下标起始位置
# 返回值
返回 enumerate(枚举) 对象
# 实例
 
```

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
     list(enumerate(seasons))
    >>>[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    list(enumerate(seasons, start=1))       # 下标从 1 开始
    >>> [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

```