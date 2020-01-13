---
layout:     post
title:      C_Function
date:       2020-01-13
author:     Louis
categories: Program_Study

---
<!-- MarkdownTOC -->




# 关于C语言的几个函数

## gets()
gets()函数从流中读取字符串，直到出现换行符或读到文件尾为止，最后加上NULL作为字符串结束。所读取的字符串暂存在给定的参数string中。

```
#include <stdio.h>
int main(void)
{
    char str[10];
    printf("Input a string.\n");
    gets(str);
    printf("The string you input is: %s",str);    //输出所有的值，注意a
}
```



