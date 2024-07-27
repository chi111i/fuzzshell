# fuzzshell

![image-20240726143653735](https://s2.loli.net/2024/07/26/IWk2m1xzDrMptYg.png)

## 使用
（视频教程）
![Sample Video](https://private-user-images.githubusercontent.com/117554817/352714100-cffaff44-07bf-445a-8a2e-f23265085b81.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIwNzQ4NjgsIm5iZiI6MTcyMjA3NDU2OCwicGF0aCI6Ii8xMTc1NTQ4MTcvMzUyNzE0MTAwLWNmZmFmZjQ0LTA3YmYtNDQ1YS04YTJlLWYyMzI2NTA4NWI4MS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcyN1QxMDAyNDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04NWE2YTEzZWY1ZWM2NjZkNjA3MzllMzNjYTdiNGZiM2I4ZTY3ZDQxZDg0YmZkZGFhZTBlM2RjNDczZjk1YjUxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.s5x6kfwiU-OPoNnT-GWHyyklOF3ESSztRx_9pcDlT04)



第一行为输入命令，文件地址，或者其他数据

第二行为黑名单，用 "," 隔开如： flag,eval,cat,system

然后点击去重。

点击复制后导入到burpsuite进行fuzz





- 命令混淆： 对linux命令进行简单的混淆
- 读文件+混淆： 不需要输入命令，输入文件的地址即可如/flag (或者/f* /f???)
- 读文件：只输出一些能查看文件的命令不进行混淆
- php读文件：题目环境存在include()文件包含的情况下使用
- php代码执行：题目环境中存在eaval()等情况下使用
- 八进制编码：
- 十六进制编码：
- IP编码：ipv4地址编码，SSRF使用
