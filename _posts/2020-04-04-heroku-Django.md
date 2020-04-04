---
layout: post
title:  python 高阶
date:   2019-03-06
categories: Python
---

<!-- MarkdownTOC -->




#heroku-Django部署

在官方文档输入
> git push heroku master

出现认证错误

这是查阅stack flow解决
> git push https://heroku:$HEROKU_API_KEY@git.heroku.com/$HEROKU_APP_NAME.git HEAD:master

$HEROKU_API_KEY:可通过https://dashboard.heroku.com/account查询

![API key](https://s1.ax1x.com/2020/04/04/GwtI6H.png)

点击reveal即可查看API key
$HEROKU_APP_NAME:就是heroku create创建的app名字

生成requirements.txt
> pip freeze > requirements.txt


