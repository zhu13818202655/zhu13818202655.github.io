---
layout: post
title: python type-hints
date:   2019-04-27
categories: python
---

<!-- MarkdownTOC -->




[官方文档][1]
**type hints are just hints, 所以只做提示不做检查.**

有时需要添加包才可使用，这与编译器有关
> from typing import List,Tuple,Set 

```
def add_unicode_checkmark(text: Text) -> Text:
    return text + u' \u2713'
```
输入输出都可以提示

[在Pycharm中使用][2]


  [1]: https://docs.python.org/3/library/typing.html
  [2]: https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html