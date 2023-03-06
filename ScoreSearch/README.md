## python 部分

### 更改 cookies

打开成绩查询页面，按下 F12 键，选择网络，点击按成绩查询，点击响应的请求，选择 cookies，复制值，在双引号内填入自己的 cookies

![img](https://img2023.cnblogs.com/blog/2770491/202303/2770491-20230306212014234-1646061268.png)

![img](https://img2023.cnblogs.com/blog/2770491/202303/2770491-20230306211440086-1344138205.png)

### 查询字符串参数

将 parmas 参数中的学号和姓名替换成自己的

![img](https://img2023.cnblogs.com/blog/2770491/202303/2770491-20230306212505873-1577056589.png)

### 表单数据

将 data 中的相关信息进行替换
![img](https://img2023.cnblogs.com/blog/2770491/202303/2770491-20230306212947836-1293008502.png)

**\_\_VIEWSTATE** 十分重要，注意保密，在浏览器控制台中将\_\_VIEWSTATE 值复制替换

**\_\_VIEWSTATEGENERATOR** 浏览器中对应的值进行替换

**ddlXN** 学年

**ddlXQ** 学期

**Button1** 查询方式

注意：按学期查询键为 `Button1`，值为 `按学期查询`；按学年查询键为`Button5`，值为 `按学年查询`；在校学习成绩查询键为 `Button2`，值为 `在校学习成绩查询`；查询已修课程最高成绩键为 `Button6`，值为 `查询已修课程最高成绩`。

![img](https://img2023.cnblogs.com/blog/2770491/202303/2770491-20230306212716581-1050201634.png)

## shell 部分

![img](https://img2023.cnblogs.com/blog/2770491/202303/2770491-20230306214220642-1450514412.png)

程序运行地址的格式为 `python地址 程序文件地址`，如我的为：

```
D:\Files\Projects\Pycharm_Projects\ScrapyLearning\venv\Scripts\python.exe D:\Files\Projects\Pycharm_Projects\ScrapyLearning\my_score.py
```

设置完之后将 cmd 文件放置桌面即可，双击运行
