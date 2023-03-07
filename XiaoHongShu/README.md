女朋友经常刷小红书，但是小红书自带的图片保存总是有水印，还要用其他软件去水印，费时费力，因此写了个小爬虫来帮女朋友下载小红书的无水印图片

**重要：在 pyw 文件的目录地址处，一定要有 pic 文件夹，否则图片会下载失败**

将 `cookies` 的内容替换成自己的 cookies，手机分享链接，电脑浏览器打开链接，按下 `F12`，在网络选项下刷新页面选择 cookies 即可，方法与[查询成绩替换 cookies 类似](https://github.com/bellongyan/MyToolsInNTU/tree/main/ScoreSearch#%E6%9B%B4%E6%94%B9-cookies)

![img](https://img2023.cnblogs.com/blog/2770491/202303/2770491-20230307085135606-1533073783.png)

使用了 `tkinter` 包，更方便使用，如果需要打包成 exe 可以使用 `pyinstaller` 包将其打包
