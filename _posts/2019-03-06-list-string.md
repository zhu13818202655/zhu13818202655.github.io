---
layout: post
title:  字符串与列表类型互换
date:   2019-03-06
categories: Python
---

<!-- MarkdownTOC -->




1. 字符串转列表（str---list)

    **运用.split方法**

    ```
    sentence = 'My dog sleeps on sofa'
    wordList = sentence.split(' ')
    ```

2. 列表转字符串（list---str)

    **运用.join方法**

    ```
    namesList = ['Tuffy','Ali','Nysha','Tim' ]
    names = ';'.join(namesList)
    ```
    
3. 算属运算符+和*用于字符串

    ```
    additionExample = 'ganehsa' + 'ganesha' + 'ganesha'
    multiplicationExample = 'ganesha' * 2
    print('Text Additions :', additionExample)
    print('Text Multiplication :', multiplicationExample)
    ```
    
    **结果**
    
    ```
    Text Additions : ganehsaganeshaganesha
    Text Multiplication : ganeshaganesha
    ```
    
4. 字符串索引

    ```
    str = 'ZXCVBNMASDFGHJKL'
    print(str[:4])#打印出第0-3个字符
    print(str[5:])#打印出第6-结束个字符
    print(str[5:9])#打印出第5-9个字符
    print(str[-1])#打印出倒数第一个字符
    ```
    
    

