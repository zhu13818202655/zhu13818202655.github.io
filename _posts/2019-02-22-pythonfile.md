---
layout:     post
title:      Python 文档处理
date:       2019-2-22
author:     Louis
categories: Python

---
<!-- MarkdownTOC -->




## **OS 模块**

1. os.path.exists(path)
文件是否存在，返回值：True False。

2. os.walk（top，topdown = True，onerror = None，followlinks = False ）
通过从上到下或从下到上遍历树来生成目录树中的文件名。对于以目录top（包括top本身）为根的树中的每个目录 ，它产生一个3元组。(dirpath, dirnames, filenames)；
topdown = True:从上到下遍历树来生成目录树中的文件名
topdown = Fals:从下到上遍历树来生成目录树中的文件名

    下面示例显示起始目录下每个目录中的非目录文件占用的字节数，但它不在任何CVS子目录下查看
    
    ```
    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('C:\学习\通信原理'):
        print(root, "consumes", end=" ")
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
    ```

3. os.scandir（path ='.' ）
返回os.DirEntry与path给出的目录中的条目对应的对象的迭代器。这些条目产生以任意顺序，特殊项目'.'和'..'不包括在内。
下面三个方法返回值都是bool类型
 - is_file
 - is_dir()
 - is_symlink()
4. 重命名
* os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)，dst不能是目录
* os.renames() 方法用于递归重命名目录或文件，该方法没有返回值
* os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)，dst不能是目录
5. os.getcwd()
当前Python脚本工作的目录路径
6. os.mkdir("file")  #创建目录
7. os.remove(file)   #进行移除文件
8. os.rmdir(dir)     #进行移除目录
9. 使用python  pathlib模块 
    **统计某一文件夹下文件数量** 

    ```
    from pathlib import Path
    dir_path = ' '
    print(len(list(Path(dir_path).iterdir())))
    ```
10. os.path.getsize（filename）#获取文件大小







