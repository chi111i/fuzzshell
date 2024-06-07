# fuzzshell

# fuzzshell开发记录

## shell类

> 

### 开发进度

- [x] 空格替换为$IFS
- [x] 空格替换为${IFS}
- [ ] 空格替换为$IFS$9
- [x] 空格替换为 <
- [ ] 空格替换为 <>
- [x] ca\t /f\lag
- [ ] 利用环境变量注入
- [x] base64编码
- [x] hex编码
- [ ] 双hex 编码
- [x] 大写hex 编码
- [x] 八进制编码 例：`echo -e "\0154\0163\0012"`
- [x] {cat,/flag}



## PHP类

### 开发进度

- [ ] 无

## 使用

![image-20240607185817466](https://s2.loli.net/2024/06/07/tQRWOLuqphHUfYj.png)

第一行为输入命令，文件地址，或者其他数据

第二行为黑名单，用 "," 隔开

记得去重。点击复制后导入到burpsuite进行fuzz
