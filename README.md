# Small_Little_Cage 抓鸡啦！
小黑屋，专门收集肉鸡的ip地址

## 简介
这是一个专门反向抓肉鸡的程序，用于收集攻击者的ip地址然后制作成为自己防御的iptables。从而达到拒绝被攻击的地步，同时通过数据收集，进行反向攻击肉鸡作为中间机器获取其机器权限的作用

## 使用方法
暂时不支持其他的服务器使用，仅限我的服务器单独使用，现在还在开发通用版本
运行代码

```
python autoban.py
```
## TO-DO 
先把每行的数据处理成list 然后再转换为dic ---done

把text file 利用python 进行处理 放入Dictionary 做成出现字典 --done

分析出现次数 进行ban人行为，同时收集尝试的用户名，作为未来的攻击字典使用 --doing

将收集过来的出现字典ip地址分析出来，进行处理和过滤

其中ip地址有可能为域名的形式出现，利用python进行转换

如果有可能就进行反向抓肉鸡的程序，这是一个很长的过程

每次处理完就要删掉现有的btmp文件以免重复统计

若成功反向抓鸡，运行同样的程序来继续抓鸡，看看最终的攻击者是谁。

``` 
Set your username: git config --global user.name "FIRST_NAME LAST_NAME"
Set your email address: git config --global user.email "MY_NAME@example.com"
```
