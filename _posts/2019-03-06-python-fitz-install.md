---
layout: post
title:  fitz包 install
date:   2019-03-06
categories: Python  
---

<!-- MarkdownTOC -->




今天想写一个图片转PDF文件的python程序，在网上找到相应教程，需要import fitz.于是用pycharm自带的下载包工具

![pycharm自带的下载包工具](https://github.com/zhu13818202655/zhu13818202655.github.io/raw/master/img/pycharm%E4%B8%8B%E8%BD%BD%E5%8C%85%E7%95%8C%E9%9D%A2.PNG)

发现安装不了，于是去官网下载此包：**https://pypi.org/project/fitz/0.0.1.dev2/#files**

![官网下载fitz](https://github.com/zhu13818202655/zhu13818202655.github.io/raw/master/img/fitz%E5%8C%85%E4%B8%8B%E8%BD%BD%E5%AE%98%E7%BD%91.PNG)

## 如何安装.whl文件

1. 下载.whl文件
2. 在命令行中输入：pip install *********.whl(绝对路径)

**但是**

经过上面操作总是出现报错：**Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Bui"**
经过一番折腾，发现需要下载**Visual C++ Build Tools** , 这是参考：【
Microsoft Visual C++ Build Tools下载/解决Visual C++ 14.0 is required问题】https://blog.csdn.net/bbhdeal/article/details/81144783
去官网**https://devblogs.microsoft.com/python/unable-to-find-vcvarsall-bat/**,下载了

![Visual C++ Build Tools 2015](https://github.com/zhu13818202655/zhu13818202655.github.io/raw/master/img/Visual%202015.PNG)

下载安装，文件比较大，重启电脑后成功。

再次在在命令行中输入：pip install *********.whl(绝对路径)
**成功！！！**

## 在虚拟环境中安装包cmd方法
    
    cd C:\myworkspace\zhu13818202655.github.io\venv\Scripts#要进入Scripts文件夹中
    activate.bat #激活虚拟环境,(虚拟环境激活后，前面会有环境名称）
    python -m pip install *********  #必须要有python -m
    deactivate.bat    #退出virtualenv
    
    
    
    
    
    
   

