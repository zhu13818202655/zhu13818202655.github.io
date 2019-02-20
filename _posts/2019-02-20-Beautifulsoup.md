---
layout:     post
title:      Beautifulsoup
date:       2019-2-20
author:     Louis
catalog:    Python Crawler

---
<!-- MarkdownTOC -->




# Beautifulsoup Study

标签（空格分隔）：根据  [Beautiful Soup 4.2.0 文档][1]学习


  [1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id4 



---
使用BeautifulSoup
```
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)
print(soup.prettify()) #按照标准的缩进格式的结构输出
```

tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用`replace_with()` 方法:
```
tag.string.replace_with("No longer bold")
tag
# <blockquote>No longer bold</blockquote>
```

通过点取属性的方式只能获得当前名字的第一个tag:
```
soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```

`find_all()` 可以找到所有你要找到的tag标签

soup.find_all('a')
```
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
tag的 .contents 属性可以将tag的子节点以列表的方式输出，输出节点内容:
```
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents
[<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# [u'The Dormouse's story']
```

**<title>标签也包含一个子节点:字符串 “The Dormouse’s story”,这种情况下字符串 “The Dormouse’s story”也属于<head>标签的子孙节点**
```
for child in head_tag.descendants:
    print(child)
    # <title>The Dormouse's story</title>
    # The Dormouse's story
```
## **.string**
1. 字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串
如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 `.string` 得到子节点:
```
title_tag.string
# u'The Dormouse's story'
```
2. 如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:
```
head_tag.contents
# [<title>The Dormouse's story</title>]

head_tag.string
# u'The Dormouse's story'
```

3. 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None,此时可以使用`.strings`来循环获取:
```
for string in soup.strings:
    print(repr(string))
```
输出的字符串中可能包含了很多空格或空行,使用`.stripped_strings`可以去除多余空白内容:








