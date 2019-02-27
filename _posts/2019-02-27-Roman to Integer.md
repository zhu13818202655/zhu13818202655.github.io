---
layout: post
title:  Roman to Integer
date:   2019-02-27
categories: Python Algorithm
---

<!-- MarkdownTOC -->




## 题目

![罗马数字转换阿拉伯数字](C:\图片\screencapture-leetcode-cn-problems-roman-to-integer-2019-02-27-14_34_34.png)

## 思路

主要是数据的存储和相邻之间加减的处理。
1. 数组存储取出,字典存储罗马数字代表的阿拉伯数字
2. 前后罗马数字比较，进行加减处理
    * 用pre 和 cur 分别记住当前数字和前一个数字，以便进行比较
    * 用数组的[i]和[i-1]

## 代码

```
def romanToInt1(s):
    result = 0
    curr = 0
    pre = 0
    for i in range(len(s)):
        if s[i] == 'I':
            curr = 1
        elif s[i] == 'V':
            curr = 5
        elif s[i] == 'X':
            curr = 10
        elif s[i] == 'L':
            curr = 50
        elif s[i] == 'C':
            curr = 100
        elif s[i] == 'D':
            curr = 500
        elif s[i] == 'M':
            curr = 1000
        result = result + curr
        if (pre < curr):
            result = result - 2 * pre
        pre = curr
    return result
```

或者

```
def romanToInt1(s):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0

    for i in range(len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            result-= d[s[i]]
        else:
            result+=d[s[i]]

    result+=d[s[len(s)-1]]
    return result


```

