---
layout: post
title: python装饰器
date:   2019-04-25
categories: python
---

<!-- MarkdownTOC -->




# Python装饰器
今天在公众号上读了[这篇文章][1]，十分受用，讲地很清楚。
使用方法我就不重复了，说一下几个补充：

## Python函数参数的五种类型
详情见：[Python函数参数的五种类型][2]

## Python中的属性(property)
方法变成属性，只需要加上@property就可以了,同时还可以创建**setter**  **getter**
```
class Animal(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._color = 'Black'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, basestring):
            self._name = value
        else:
            self._name = 'No name'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0 and value < 100:
            self._age = value
        else:
            self._age = 0
            # print 'invalid age value.'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value;
    

a = Animal('black dog', 3)
a.name = 'white dog'
a.age = 300
print 'Name:', a.name
print 'Age:', a.age
```

作用：当你想要在原函数中增加一些功能而不想修改一个函数，你可以使用装饰器。

  [1]: https://mp.weixin.qq.com/s/KCXkOCIMzIp86tU-OJuZMg
  [2]: https://www.cnblogs.com/blackmatrix/p/6673220.html