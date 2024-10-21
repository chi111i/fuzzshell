# fuzzshell 
# 如何可以提供笔记或者WP 请加 QQ: 2741676608 助力工具开发

![图片](https://github.com/user-attachments/assets/2e4b0ccd-39c6-48cb-b65a-df22c5eb5650)

## 视频教程
视频教程: https://youtu.be/LAFNWY7c_9E 



## 使用步骤
1.第一行为输入命令，文件地址，或者其他数据

2.第二行为黑名单，用 "," 隔开如： flag,eval,cat,system ，然后点击黑名单，会清除输出中存在黑名单的数据

3.然后点击去重。

4.点击复制后导入到burpsuite进行fuzz



## 功能说明
- 黑名单 不支持正则,需要将被过滤的字符用 `,` 隔开 如  ` flag,eval,cat,system,php` （注意最后面不能有`,`逗号） 然后点击黑名单，会按行清除输出中存在黑名单的数据
  
  可以用以下脚本提取
  
  python
  ``` python
  import re

  # 定义过滤规则
  pattern = r'[A-Zd-z\\. /*$#@!+^]'

  # 初始化两个列表
  filtered_chars = []
  unfiltered_chars = []

  # 遍历所有ASCII字符
  for i in range(128):
      char = chr(i)
      if re.search(pattern, char):
          filtered_chars.append(char)
      else:
          unfiltered_chars.append(char)

  #print("Filtered characters:", filtered_chars)
  for i in filtered_chars:
      print(i, end=",")
  #print("Unfiltered characters:", unfiltered_chars)

  ```
  php
  ``` php
  $filtered_chars = [];

  for ($ascii = 0; $ascii < 256; $ascii++) {
      if (!preg_match('/[A-Za-z0-9]|\'|"|`|\ |,|\.|-|\+|=|\/|\\|<|>|\$|\?|\^|&|\|/is', chr($ascii))) {
         $filtered_chars[] = chr($ascii);
    }
  }

  echo implode(',', $filtered_chars);
  ```
  
- 命令混淆： 对linux命令进行简单的混淆 `cat /flag` >> &#96;echo 636174202f666c6167 | xxd -r -p&#96;
- 读文件+混淆： 不需要输入命令，输入文件的地址即可如/flag (或者/f* /f???) 
- 读文件：只输出一些能查看文件的命令不进行混淆 不需要输入命令，输入文件的地址即可如/flag
- php读文件：题目环境存在include()文件包含的情况下使用 不需要输入命令，输入文件的地址即可如/flag
- php代码执行：题目环境中存在eval()等情况下使用

加入了 无字母数字RCE(异或和取反等方法) 以及 无参数+无字母数字RCE (类似于`system(pos(next(getallheaders())));` >>` [~%8C%86%8C%8B%9A%92][!%FF]([~%8F%90%8C][!%FF]([~%91%9A%87%8B][!%FF]([~%98%9A%8B%9E%93%93%97%9A%9E%9B%9A%8D%8C][!%FF]())));`)
- 八进制编码：
- 十六进制编码：
- IP编码：ipv4地址编码，SSRF使用
- 沙箱逃逸：参考https://github.com/Macr0phag3/parselmouth ,  在第一栏输入`__import__('os').popen('cat /flag').read()` 第二栏输入黑名单  `__,os,pop,system` 点击输出自动绕WAF
- SSTI：参考https://github.com/Marven11/Fenjing ， 在第一栏输入 `cat /flag` 第二栏输入  `_,os,{{,}},eavl,subprocess` 点击输出自动绕WAF
- phpinfo信息 ：如果存在phpinfo页面，可以将burpsuite的数据包内容 或者 浏览器右键查看页面源代码全选 复制到第一栏 ，点击输出即可 参考  https://github.com/LxxxSec/HackPhpinfo

## 微步

  ![图片](https://github.com/user-attachments/assets/a0a6f2e0-6724-4ce4-b4da-b19024a8b7fa)
  
## 请我喝菠萝甜心橙
![图片](https://github.com/user-attachments/assets/2c65dd24-52c4-4e25-aaff-4aae5938fa2c)

