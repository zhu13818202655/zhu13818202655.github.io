---
layout:     post
title:      Beautifulsoup Study
date:       2019-2-20
author:     Louis
catalog:    python-crawler

---
<!-- MarkdownTOC -->




# Beautifulsoup Study

标签（空格分隔）：Crowler Python
根据[eautiful Soup 4.2.0 文档][1]学习
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
输出的字符串中可能包含了很多空格或空行,使用`.stripped_strings`可以去除多余空白内容.

**`find_all`查找文档中所有匹配标签**
 - 字符串
如果传入字节码参数,Beautiful Soup会当作UTF-8编码,可以传入一段Unicode 编码来避免Beautiful Soup解析编码出错
 - 正则表达式
 - 列表
如果传入列表参数,BeautifulSoup会将与列表中任一元素匹配的内容返回.
```
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
 - True
True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
 - 可以自定义函数方法
 - 使用多个指定名字的参数可以同时过滤tag的多个属性:
```
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
```
- 通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
> data_soup.find_all(attrs={"data-foo": "value"})

- limit限制
> soup.find_all("a", limit=2)

- 调用tag的 find_all() 方法时,BeautifulSoup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .

## CSS选择器
在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数,即可使用CSS选择器的语法找到tag

通过tag标签逐层查找:
```
soup.select("html head title")
# [<title>The Dormouse's story</title>]
```
找到某个tag标签下的直接子标签 [6] :
```
soup.select("head > title")
# [<title>The Dormouse's story</title>]

soup.select("p > a:nth-of-type(2)")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select("p > #link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

找到兄弟节点标签:
```
# ~表示所有其他兄弟标签, link1前面的#，表示查找对应的#id,sister前面的.，表示查找对应的
soup.select("#link1 ~ .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie"  id="link3">Tillie</a>]

soup.select("#link1 + .sister")//+ 表示第一个其他兄弟标签
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

通过tag的id查找:
```
soup.select("a#link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

## 格式化输出
prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行
```
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
soup.prettify()
# '<html>\n <head>\n </head>\n <body>\n  <a href="http://example.com/">\n...'
print(soup.prettify())
# <html>
#  <head>
#  </head>
#  <body>
#   <a href="http://example.com/">
#    I linked to
#    <i>
#     example.com
#    </i>
#   </a>
#  </body>
# </html>
```


## get_text()
如果只想得到tag中包含的文本内容,那么可以嗲用 get_text() 方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回:
```
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
u'\nI linked to example.com\n'
soup.i.get_text()
u'example.com'
```
可以通过参数指定tag的文本内容的分隔符:
```
# soup.get_text("|")
u'\nI linked to |example.com|\n'
```
还可以去除获得文本内容的前后空白:
```
# soup.get_text("|", strip=True)
u'I linked to|example.com'
```
或者使用 .stripped_strings 生成器,获得文本列表后手动处理列表:
```
[text for text in soup.stripped_strings]
# [u'I linked to', u'example.com']
```

## 补充：
1. 使用Beautiful Soup解析后,文档都被转换成了Unicode
2. Beautiful Soup输出文档时,不管输入文档是什么编码方式,输出编码均为UTF-8编码,


  [1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id4
