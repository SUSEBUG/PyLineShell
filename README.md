### [English/英文](README_en.md)

<div align="center"> <img src="bugctf.png" width = 135 height = 99 /></div>
<p align="center">PyLineShell: 一个基于Python3的个人Shell Payload库</p>


PyLineShell是一个基于Python3的个人Shell Payload库，适用于在Python Web应用拿到exec、pickle命令执行点后的渗透阶段. 用户可以调用Python文件来生成需要的Payload.

🔍生成的Payload基本上为简单的一行长代码，主要针对于无法赋值、无法多行输入的命令执行点. 

💡对于绝大部分应用(Web应用、框架)，都可以一键命令执行和一键写入代码

🦙这是我自己的一个练手项目，希望大佬多多包涵. 可以提issue反馈问题

# 快速开始

使用Python生成一个普通版执行命令的Payload

![测试1](https://s21.ax1x.com/2024/03/25/pF4It1g.png)

使用Python ASCII码代码混淆器

![测试2](https://s21.ax1x.com/2024/03/25/pF4INcQ.png)

# 鸣谢

在开发的过程中，少不了以下开源/开放代码的支持

* bfengj的Flask内存马代码: https://blog.csdn.net/rfrder/article/details/121005608

* yiqing提供的部分代码  

<div align="center"> <img src="bugctf.png" width = 135 height = 99 /></div>